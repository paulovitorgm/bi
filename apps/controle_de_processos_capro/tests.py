from decimal import Decimal

from descontinuado.coordenadormodel import CoordenadorModel
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
    EsferaAdministrativa,
)


class CoordenadorModelTest(TestCase):
    def setUp(self):
        self.coordenador = CoordenadorModel(
            nome='Maria da Silva',
            matricula='123456',
        )

    def test_deve_criar_coordenador_valido(self):
        self.coordenador.full_clean()

    def test_nome_nao_pode_ser_vazio(self):
        self.coordenador.nome = ''

        with self.assertRaises(ValidationError):
            self.coordenador.full_clean()

    def test_matricula_nao_pode_ser_vazia(self):
        self.coordenador.matricula = ''

        with self.assertRaises(ValidationError):
            self.coordenador.full_clean()

    def test_str_deve_retornar_nome(self):
        self.assertEqual(
            str(self.coordenador),
            'Maria da Silva',
        )

    def test_matricula_deve_ser_unica(self):
        self.coordenador.save()

        with self.assertRaises(IntegrityError):
            CoordenadorModel.objects.create(
                nome='Outro Coordenador',
                matricula='123456',
            )


class ControleDeProcessosModelTest(TestCase):
    def setUp(self):
        self.coordenador = CoordenadorModel.objects.create(
            nome='Maria da Silva', matricula='123456'
        )

        self.processo = ControleDeProcessosModel(
            processo_sei='23106012345202411',
            modalidade=1,
            natureza=1,
            abrangencia=1,
            forma_de_aprovacao=1,
            coordenador=self.coordenador,
            custos_indiretos=Decimal('1500.50'),
            esfera_administrativa=EsferaAdministrativa.FEDERAL,
            ementa='Projeto de pesquisa',
            mes_da_aprovacao=1,
        )

    def test_deve_criar_processo_valido(self):
        self.processo.full_clean()

    def test_processo_sei_deve_ter_17_digitos(self):
        self.processo.processo_sei = '123'
        with self.assertRaises(ValidationError):
            self.processo.full_clean()

    def test_processo_sei_nao_pode_conter_letras(self):
        self.processo.processo_sei = '23106012345ABC411'

        with self.assertRaises(ValidationError):
            self.processo.full_clean()

    def test_custos_indiretos_nao_podem_ser_negativos(self):
        self.processo.custos_indiretos = -1

        with self.assertRaises(ValidationError):
            self.processo.full_clean()

    def test_processo_formatado(self):
        self.assertEqual(
            self.processo.processo_formatado,
            '23106.012345/2024-11',
        )

    def test_str_do_model(self):
        texto = str(self.processo)

        self.assertIn('Processo sei:', texto)
        self.assertIn('Projeto de pesquisa', texto)
        self.assertIn('Maria da Silva', texto)

    def test_processo_sei_deve_ser_unico(self):
        self.processo.save()

        with self.assertRaises(IntegrityError):
            ControleDeProcessosModel.objects.create(
                processo_sei='23106012345202411',
                modalidade=1,
                natureza=1,
                abrangencia=1,
                forma_de_aprovacao=1,
                coordenador=self.coordenador,
                custos_indiretos=Decimal('100'),
                esfera_administrativa=EsferaAdministrativa.FEDERAL,
                ementa='Outro processo',
                mes_da_aprovacao=2,
            )

    def test_esfera_administrativa_federal(self):
        self.assertEqual(
            self.processo.esfera_administrativa,
            EsferaAdministrativa.FEDERAL,
        )

    def test_mes_da_aprovacao(self):
        self.assertEqual(
            self.processo.mes_da_aprovacao,
            1,
        )
