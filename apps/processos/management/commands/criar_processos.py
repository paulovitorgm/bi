import random
from datetime import timedelta
from decimal import Decimal

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from faker import Faker

from apps.pessoas.models import PessoaModel
from apps.processos.models import (
    Abrangencia,
    EntidadeParceira,
    EsferaAdministrativaChoices,
    ItemPlanoDespesa,
    Modalidade,
    Natureza,
    OdsOnuChoices,
    ParticipesModel,
    ProcessoProjeto,
    PublicoPrivado,
    TipoDespesa,
    TipoInstrumento,
    TipoInstrumentoChoices,
    Unidade,
)
from apps.processos.services import recalcular_valores_totais

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Popula o banco com dados fictícios para testes.'

    def add_arguments(self, parser):  # ruff: ignore[no-self-use]
        parser.add_argument(
            '--processos',
            type=int,
            default=1000,
            help='Quantidade de processos a criar (padrão: 1000).',
        )
        parser.add_argument(
            '--pessoas',
            type=int,
            default=300,
            help='Quantidade de pessoas a criar se não houver pessoas suficientes.',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        quantidade_processos = options['processos']
        quantidade_pessoas = options['pessoas']
        if quantidade_processos < 0 or quantidade_pessoas < 0:
            raise CommandError('As quantidades não podem ser negativas.')

        self.stdout.write('Criando cadastros auxiliares...')
        self.criar_dominios()
        self.garantir_pessoas(quantidade_pessoas)
        self.criar_processos(quantidade_processos)
        self.stdout.write(self.style.SUCCESS('Banco populado com sucesso.'))

    def criar_dominios(self):  # ruff: ignore[no-self-use]
        participes = [
            ('UnB', 'Universidade de Brasília'),
            ('FINATEC', 'Fundação de Empreendimentos Científicos e Tecnológicos'),
            ('CNPQ', 'Conselho Nacional de Desenvolvimento Científico e Tecnológico'),
            ('CAPES', 'Coordenação de Aperfeiçoamento de Pessoal de Nível Superior'),
            ('MEC', 'Ministério da Educação'),
            ('FAPDF', 'Fundação de Apoio à Pesquisa do Distrito Federal'),
        ]
        for sigla, nome in participes:
            ParticipesModel.objects.get_or_create(sigla=sigla, defaults={'nome': nome})

        for sigla in [
            'FGA',
            'FT',
            'FUP',
            'FS',
            'FACE',
            'FAU',
            'FCE',
            'IQ',
            'IE',
            'IL',
            'IB',
        ]:
            Unidade.objects.get_or_create(
                sigla=sigla, defaults={'nome': f'Unidade {sigla}'}
            )

        for nome in [
            'Pesquisa',
            'Ensino',
            'Extensão',
            'Inovação',
            'Prestação de Serviços',
        ]:
            Modalidade.objects.get_or_create(nome=nome)
        for nome in ['Acadêmico', 'Tecnológico', 'Institucional', 'Internacional']:
            Natureza.objects.get_or_create(nome=nome)
        for nome in ['Local', 'Regional', 'Nacional', 'Internacional']:
            Abrangencia.objects.get_or_create(nome=nome)

        for indice in range(30):
            EntidadeParceira.objects.get_or_create(
                sigla=f'ENT{indice}',
                defaults={
                    'nome': fake.company(),
                    'publico_privado': random.choice(PublicoPrivado.values),
                },
            )

        for descricao in [
            'Auxílio Financeiro a Pesquisador',
            'Bolsa',
            'Material de Consumo',
            'Equipamentos',
            'Serviços de Terceiros PJ',
            'Serviços de Terceiros PF',
            'Passagens',
            'Diárias',
        ]:
            TipoDespesa.objects.get_or_create(descricao=descricao)

        for nome in TipoInstrumentoChoices.values:
            TipoInstrumento.objects.get_or_create(nome=nome)

    def garantir_pessoas(self, quantidade):  # ruff: ignore[no-self-use]
        if PessoaModel.objects.count() >= max(quantidade, 1):
            return
        call_command(
            'criar_pessoas', max(quantidade, 1) - PessoaModel.objects.count(), verbosity=0
        )

    def criar_processos(  # ruff: ignore[no-self-use, too-many-locals]
        self, quantidade
    ):
        if quantidade == 0:
            return

        pessoas = list(PessoaModel.objects.all())
        unidades = list(Unidade.objects.all())
        modalidades = list(Modalidade.objects.all())
        naturezas = list(Natureza.objects.all())
        abrangencias = list(Abrangencia.objects.all())
        entidades = list(EntidadeParceira.objects.all())
        participes = list(ParticipesModel.objects.all())
        tipos_despesa = list(TipoDespesa.objects.all())
        tipos_instrumento = list(TipoInstrumento.objects.all())
        existentes = set(ProcessoProjeto.objects.values_list('processo', flat=True))
        processos = []
        hoje = timezone.now().date()
        indice = ProcessoProjeto.objects.count() + 1

        while len(processos) < quantidade:
            processo = f'23106{indice:011}'
            indice += 1
            if processo in existentes:
                continue
            existentes.add(processo)
            inicio = hoje - timedelta(days=random.randint(0, 3000))
            valor_inicial = Decimal(random.randint(100000, 10000000))
            processos.append(
                ProcessoProjeto(
                    processo=processo,
                    numero_convenio=f'CV-{processo[-11:]}',
                    nome_do_processo=fake.catch_phrase(),
                    ementa=fake.paragraph(nb_sentences=4),
                    tipo_instrumento=random.choice(tipos_instrumento),
                    esfera_administrativa=random.choice(
                        EsferaAdministrativaChoices.values
                    ),
                    abrangencia=random.choice(abrangencias),
                    entidade_parceira=random.choice(entidades),
                    coordenador=random.choice(pessoas),
                    supervisor_academico=random.choice(pessoas),
                    relator=random.choice(pessoas),
                    substituto=random.choice(pessoas),
                    valor_inicial=valor_inicial,
                    valor_total=valor_inicial,
                    custos_indiretos=Decimal(random.randint(1000, 500000)),
                    dt_inicio=inicio,
                    dt_termino=inicio + timedelta(days=random.randint(180, 1800)),
                    dt_assinatura=inicio,
                    ods_onu=random.choice(OdsOnuChoices.values),
                )
            )

        criados = ProcessoProjeto.objects.bulk_create(processos, batch_size=1000)
        processo_ids = [processo.pk for processo in criados]
        through_relations = [
            (ProcessoProjeto.unidade_interessada.through, unidades, 'unidade_id'),
            (ProcessoProjeto.modalidade.through, modalidades, 'modalidade_id'),
            (ProcessoProjeto.natureza.through, naturezas, 'natureza_id'),
            (ProcessoProjeto.participes.through, participes, 'participesmodel_id'),
        ]
        for through_model, opcoes, field_name in through_relations:
            relacoes = []
            for processo in criados:
                limite = min(len(opcoes), 3 if field_name == 'unidade_id' else 2)
                quantidade_relacoes = random.randint(
                    0 if field_name == 'natureza_id' else 1, limite
                )
                for objeto in random.sample(opcoes, quantidade_relacoes):
                    relacoes.append(
                        through_model(
                            processoprojeto_id=processo.pk, **{field_name: objeto.pk}
                        )
                    )
            through_model.objects.bulk_create(relacoes, batch_size=3000)

        despesas = []
        for processo in criados:
            for tipo in random.sample(
                tipos_despesa, random.randint(1, min(4, len(tipos_despesa)))
            ):
                despesas.append(
                    ItemPlanoDespesa(
                        processo=processo,
                        tipo_despesa=tipo,
                        valor=Decimal(random.randint(5000, 300000)),
                    )
                )
        ItemPlanoDespesa.objects.bulk_create(despesas, batch_size=3000)
        recalcular_valores_totais(processo_ids)
        self.stdout.write(
            self.style.SUCCESS(f'{quantidade} processos criados com sucesso!')
        )
