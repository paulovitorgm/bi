import random
from datetime import timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from faker import Faker

from apps.pessoas.models import PessoaModel, SexoChoices
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

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Popula o banco com dados de teste.'

    def add_arguments(self, parser):  # ruff: ignore[no-self-use]
        parser.add_argument(
            '--processos',
            type=int,
            default=1000,
            help='Quantidade de processos.',
        )

        parser.add_argument(
            '--pessoas',
            type=int,
            default=300,
            help='Quantidade de pessoas.',
        )

    @transaction.atomic
    def handle(self, *args, **options):

        qtd_processos = options['processos']
        qtd_pessoas = options['pessoas']

        self.stdout.write('Criando dados auxiliares...')

        self.criar_dominios()

        self.stdout.write('Criando pessoas...')
        self.criar_pessoas(qtd_pessoas)

        self.stdout.write('Criando processos...')
        self.criar_processos(qtd_processos)

        self.stdout.write(self.style.SUCCESS('Banco populado com sucesso.'))

    # --------------------------------------------------------

    def criar_dominios(self):  # ruff: ignore[no-self-use]
        participes = [
            ('UnB', 'Universidade de Brasília'),
            ('FINATEC', 'Fundação de Empreendimentos Científicos e Tecnológicos'),
            ('CNPQ', 'Conselho Nacional de Desenvolvimento Científico e Tecnológico'),
            ('CAPES', 'Coordenação de Aperfeiçoamento de Pessoal de Nível Superior'),
            ('MEC', 'Ministério da Educação'),
            ('FAPDF', 'Fundação de Apoio à Pesquisa do Distrito Federal'),
            ('PETROBRAS', 'Petróleo Brasileiro S.A.'),
            ('EMBRAPA', 'Empresa Brasileira de Pesquisa Agropecuária'),
        ]

        for sigla, nome in participes:
            ParticipesModel.objects.get_or_create(
                sigla=sigla,
                defaults={
                    'nome': nome,
                },
            )
        unidades = [
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
        ]

        for sigla in unidades:
            Unidade.objects.get_or_create(
                sigla=sigla,
                defaults={'nome': f'Unidade {sigla}'},
            )

        modalidades = [
            'Pesquisa',
            'Ensino',
            'Extensão',
            'Inovação',
            'Prestação de Serviços',
        ]

        for nome in modalidades:
            Modalidade.objects.get_or_create(nome=nome)

        naturezas = [
            'Acadêmico',
            'Tecnológico',
            'Institucional',
            'Internacional',
        ]

        for nome in naturezas:
            Natureza.objects.get_or_create(nome=nome)

        abrangencias = [
            'Local',
            'Regional',
            'Nacional',
            'Internacional',
        ]

        for nome in abrangencias:
            Abrangencia.objects.get_or_create(nome=nome)

        for i in range(30):
            EntidadeParceira.objects.get_or_create(
                sigla=f'ENT{i}',
                defaults={
                    'nome': fake.company(),
                    'publico_privado': random.choice([
                        PublicoPrivado.PUBLICO,
                        PublicoPrivado.PRIVADO,
                    ]),
                },
            )
        tipos_despesa = [
            'Auxílio Financeiro a Pesquisador',
            'Bolsa',
            'Material de Consumo',
            'Equipamentos',
            'Serviços de Terceiros PJ',
            'Serviços de Terceiros PF',
            'Passagens',
            'Diárias',
        ]

        for descricao in tipos_despesa:
            TipoDespesa.objects.get_or_create(descricao=descricao)

        for nome in TipoInstrumentoChoices.values:
            TipoInstrumento.objects.get_or_create(nome=nome)

    # --------------------------------------------------------

    def criar_pessoas(self, quantidade):  # ruff: ignore[no-self-use]

        if PessoaModel.objects.exists():
            return

        pessoas = []

        for i in range(quantidade):
            sexo = random.choice([
                SexoChoices.MASC,
                SexoChoices.FEM,
            ])

            if sexo == SexoChoices.MASC:
                nome = fake.name_male()
            else:
                nome = fake.name_female()

            pessoas.append(
                PessoaModel(
                    matricula=str(100000 + i),
                    nome=nome,
                    sexo=sexo,
                )
            )

        PessoaModel.objects.bulk_create(
            pessoas,
            batch_size=1000,
        )

    # --------------------------------------------------------

    def criar_processos(self, quantidade):  # ruff: ignore[no-self-use, too-many-locals]

        pessoas = list(PessoaModel.objects.all())

        unidades = list(Unidade.objects.all())

        modalidades = list(Modalidade.objects.all())

        naturezas = list(Natureza.objects.all())

        abrangencias = list(Abrangencia.objects.all())

        entidades = list(EntidadeParceira.objects.all())

        participes = list(ParticipesModel.objects.all())

        tipos_despesa = list(TipoDespesa.objects.all())
        tipos_instrumento = list(TipoInstrumento.objects.all())

        processos = []

        hoje = timezone.now().date()
        offset = ProcessoProjeto.objects.count()

        for i in range(quantidade):
            indice_unico = offset + i + 1
            inicio = hoje - timedelta(days=random.randint(0, 3000))
            termino = inicio + timedelta(days=random.randint(180, 1800))

            processos.append(
                ProcessoProjeto(
                    processo=f'23106{indice_unico:011}',
                    numero_convenio=f'CV-{indice_unico}',
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
                    valor_total=Decimal(random.randint(100000, 10000000)),
                    custos_indiretos=Decimal(random.randint(1000, 500000)),
                    dt_inicio=inicio,
                    dt_termino=termino,
                    dt_assinatura=inicio,
                    ods_onu=random.choice(OdsOnuChoices.values),
                )
            )

        criados = ProcessoProjeto.objects.bulk_create(
            processos,
            batch_size=1000,
        )

        through_unidade = ProcessoProjeto.unidade_interessada.through
        through_modalidade = ProcessoProjeto.modalidade.through
        through_natureza = ProcessoProjeto.natureza.through
        through_participes = ProcessoProjeto.participes.through

        rel_unidades = []
        rel_modalidades = []
        rel_naturezas = []
        rel_participes = []

        for processo in criados:
            for unidade in random.sample(
                unidades,
                random.randint(1, 3),
            ):
                rel_unidades.append(
                    through_unidade(
                        processoprojeto_id=processo.id,
                        unidade_id=unidade.id,
                    )
                )

            for modalidade in random.sample(
                modalidades,
                random.randint(1, 2),
            ):
                rel_modalidades.append(
                    through_modalidade(
                        processoprojeto_id=processo.id,
                        modalidade_id=modalidade.id,
                    )
                )

            for natureza in random.sample(
                naturezas,
                random.randint(0, 2),
            ):
                rel_naturezas.append(
                    through_natureza(
                        processoprojeto_id=processo.id,
                        natureza_id=natureza.id,
                    )
                )

            for participe in random.sample(
                participes,
                random.randint(2, 5),
            ):
                rel_participes.append(
                    through_participes(
                        processoprojeto_id=processo.id,
                        participesmodel_id=participe.id,
                    )
                )

        through_unidade.objects.bulk_create(
            rel_unidades,
            batch_size=3000,
        )

        through_modalidade.objects.bulk_create(
            rel_modalidades,
            batch_size=3000,
        )

        through_natureza.objects.bulk_create(
            rel_naturezas,
            batch_size=3000,
        )

        through_participes.objects.bulk_create(
            rel_participes,
            batch_size=3000,
        )

        despesas = []

        for processo in criados:
            quantidade = random.randint(3, 8)

            tipos = random.sample(
                tipos_despesa,
                min(quantidade, len(tipos_despesa)),
            )

            for tipo in tipos:
                despesas.append(
                    ItemPlanoDespesa(
                        processo=processo,
                        tipo_despesa=tipo,
                        valor=Decimal(random.randint(5000, 300000)),
                    )
                )

        ItemPlanoDespesa.objects.bulk_create(
            despesas,
            batch_size=3000,
        )
