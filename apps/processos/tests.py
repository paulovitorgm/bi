import json
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse

from apps.pessoas.models import PessoaModel
from apps.processos.forms.processoprojetoform import (
    ProcessoProjetoForm,
    TermoAditivoInlineForm,
)
from apps.processos.models import Modalidade, ProcessoProjeto, TipoInstrumento, Unidade
from apps.processos.models.choices import EsferaAdministrativaChoices, OdsOnuChoices
from apps.processos.models.termosadtivos import TermosAdtivos
from apps.processos.services import recalcular_valores_totais


class ProcessoAPITests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username='api-teste', password='senha-segura'
        )
        self.tipo_instrumento = TipoInstrumento.objects.create(nome='Convênio')
        self.unidade = Unidade.objects.create(sigla='FGA', nome='Faculdade do Gama')
        self.modalidade = Modalidade.objects.create(nome='Pesquisa')
        self.lista_url = reverse('api-processo-list')
        self.payload = {
            'processo': '2310600000000001',
            'nome_do_processo': 'Projeto de teste',
            'tipo_instrumento': self.tipo_instrumento.pk,
            'unidade_interessada': [self.unidade.pk],
            'modalidade': [self.modalidade.pk],
            'esfera_administrativa': EsferaAdministrativaChoices.FEDERAL,
            'ods_onu': OdsOnuChoices.ODS_4,
            'valor_inicial': '100.00',
            'valor_total': '999.99',
        }

    def post_json(self, url, payload):
        return self.client.post(url, json.dumps(payload), content_type='application/json')

    def test_api_exige_autenticacao(self):
        response = self.client.get(self.lista_url)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_cria_processo_e_ignora_valor_total_enviado(self):
        self.client.force_login(self.usuario)

        response = self.post_json(self.lista_url, self.payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['valor_total'], '100.00')
        processo = ProcessoProjeto.objects.get(processo=self.payload['processo'])
        self.assertEqual(processo.valor_inicial, Decimal('100.00'))
        self.assertEqual(processo.valor_total, Decimal('100.00'))

    def test_termo_aditivo_recalcula_total_do_processo(self):
        self.client.force_login(self.usuario)
        self.post_json(self.lista_url, self.payload)
        processo = ProcessoProjeto.objects.get(processo=self.payload['processo'])

        response = self.post_json(
            reverse('api-termo-aditivo-list'),
            {'processo': processo.pk, 'termo': '1º Termo Aditivo', 'valor': '25.50'},
        )

        self.assertEqual(response.status_code, 201)
        processo.refresh_from_db()
        self.assertEqual(processo.valor_total, Decimal('125.50'))

    @override_settings(CORS_ALLOWED_ORIGINS=['https://front.exemplo.gov.br'])
    def test_cors_permite_origem_configurada_e_header_de_autorizacao(self):
        response = self.client.options(
            self.lista_url,
            HTTP_ORIGIN='https://front.exemplo.gov.br',
            HTTP_ACCESS_CONTROL_REQUEST_METHOD='GET',
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(
            response.headers['Access-Control-Allow-Origin'],
            'https://front.exemplo.gov.br',
        )
        self.assertIn('Authorization', response.headers['Access-Control-Allow-Headers'])


class RecalculoEmMassaTests(TestCase):
    def test_recalcula_total_apos_inclusao_em_massa_de_termos(self):
        usuario = get_user_model().objects.create_user(
            username='carga-teste', password='senha-segura'
        )
        tipo_instrumento = TipoInstrumento.objects.create(nome='Acordo')
        unidade = Unidade.objects.create(sigla='FT', nome='Faculdade de Tecnologia')
        modalidade = Modalidade.objects.create(nome='Extensão')
        processo = ProcessoProjeto.objects.create(
            processo='2310600000000002',
            nome_do_processo='Carga em massa',
            tipo_instrumento=tipo_instrumento,
            esfera_administrativa=EsferaAdministrativaChoices.FEDERAL,
            ods_onu=OdsOnuChoices.ODS_4,
            valor_inicial=Decimal('100.00'),
            criado_por=usuario,
            atualizado_por=usuario,
        )
        processo.unidade_interessada.add(unidade)
        processo.modalidade.add(modalidade)

        TermosAdtivos.objects.bulk_create([
            TermosAdtivos(processo=processo, termo='Carga 1', valor=Decimal('10.00')),
            TermosAdtivos(processo=processo, termo='Carga 2', valor=Decimal('15.00')),
        ])
        recalcular_valores_totais([processo.pk])

        processo.refresh_from_db()
        self.assertEqual(processo.valor_total, Decimal('125.00'))


class ValidacaoProcessoFormTests(TestCase):
    def setUp(self):
        self.tipo_instrumento = TipoInstrumento.objects.create(nome='Contrato')
        self.unidade = Unidade.objects.create(sigla='FGA', nome='Faculdade do Gama')
        self.modalidade = Modalidade.objects.create(nome='Pesquisa')
        self.pessoa = PessoaModel.objects.create(nome='Pessoa Teste')

    def dados_processo(self, **alteracoes):
        dados = {
            'processo': '2310600000000003',
            'nome_do_processo': 'Processo de teste',
            'tipo_instrumento': self.tipo_instrumento.pk,
            'esfera_administrativa': EsferaAdministrativaChoices.FEDERAL,
            'unidade_interessada': [self.unidade.pk],
            'modalidade': [self.modalidade.pk],
            'valor_inicial': '100.00',
            'custos_indiretos': '0.00',
            'dt_assinatura': '2026-01-10',
            'dt_inicio': '2026-01-10',
            'dt_termino': '2026-01-10',
        }
        dados.update(alteracoes)
        return dados

    def test_permite_datas_no_mesmo_dia(self):
        form = ProcessoProjetoForm(data=self.dados_processo())

        self.assertTrue(form.is_valid(), form.errors)

    def test_rejeita_inicio_anterior_a_assinatura(self):
        form = ProcessoProjetoForm(
            data=self.dados_processo(dt_inicio='2026-01-09')
        )

        self.assertIn('dt_inicio', form.errors)

    def test_rejeita_termino_anterior_a_assinatura_e_inicio(self):
        form = ProcessoProjetoForm(
            data=self.dados_processo(
                dt_inicio='2026-01-11',
                dt_termino='2026-01-09',
            )
        )

        self.assertIn('dt_termino', form.errors)
        self.assertGreaterEqual(len(form.errors['dt_termino']), 2)

    def test_rejeita_pessoa_em_mais_de_um_papel(self):
        form = ProcessoProjetoForm(
            data=self.dados_processo(
                coordenador=self.pessoa.pk,
                relator=self.pessoa.pk,
            )
        )

        self.assertIn('coordenador', form.errors)
        self.assertIn('relator', form.errors)


class ValidacaoTermoAditivoFormTests(TestCase):
    def test_permite_assinatura_no_mesmo_dia_do_termino(self):
        form = TermoAditivoInlineForm(
            data={
                'termo': 'Termo 1',
                'dt_assinatura': '2026-01-10',
                'dt_termino': '2026-01-10',
                'valor': '10.00',
            }
        )

        self.assertTrue(form.is_valid(), form.errors)

    def test_rejeita_assinatura_posterior_ao_termino(self):
        form = TermoAditivoInlineForm(
            data={
                'termo': 'Termo 2',
                'dt_assinatura': '2026-01-11',
                'dt_termino': '2026-01-10',
                'valor': '10.00',
            }
        )

        self.assertIn('dt_termino', form.errors)
