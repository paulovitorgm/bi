import random
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
    EsferaAdministrativa,
)
from apps.pessoas.models import PessoaModel

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Cria pessoas se necessário e gera processos fictícios em lote.'

    def add_arguments(self, parser):  # ruff: ignore[no-self-use]
        parser.add_argument('quantidade', type=int, help='Quantidade de processos.')

    def handle(self, *args, **options):
        quantidade = options['quantidade']

        # 1. Garante que existem registros suficientes
        self._garantir_coordenadores(minimo=20)

        # 2. Extrai explicitamente os IDs reais direto da tabela mapeada no banco
        coordenadores_ids = list(PessoaModel.objects.values_list('id', flat=True))

        if not coordenadores_ids:
            raise CommandError('Nenhum coordenador encontrado na tabela.')

        processos = []

        for _ in range(quantidade):
            # Atribui diretamente o ID numérico mapeado do banco de dados real
            id_escolhido = random.choice(coordenadores_ids)

            processos.append(
                ControleDeProcessosModel(
                    processo_sei=fake.unique.numerify('#################'),
                    modalidade=random.randint(1, 3),
                    natureza=random.randint(1, 4),
                    abrangencia=random.randint(1, 3),
                    forma_de_aprovacao=random.randint(1, 3),
                    coordenador_id=id_escolhido,  # Atribuição explícita por ID da FK
                    custos_indiretos=Decimal(f'{random.uniform(0, 50000):.2f}'),
                    esfera_administrativa=random.choice(EsferaAdministrativa.values),
                    ementa=fake.sentence(nb_words=8),
                    data_da_aprovacao=fake.date_between(
                        start_date='-5y', end_date='today'
                    ),
                    valor_do_contrato=Decimal(f'{random.uniform(0, 50000):.2f}'),
                )
            )

        ControleDeProcessosModel.objects.bulk_create(processos)

        self.stdout.write(
            self.style.SUCCESS(f'{quantidade} processos criados com sucesso!')
        )

    def _garantir_coordenadores(self, minimo=20):
        total_atual = PessoaModel.objects.count()

        if total_atual < minimo:
            faltam = minimo - total_atual
            self.stdout.write(
                self.style.WARNING(
                    f'Cadastrando {faltam} novas pessoas para suprir os coordenadores...'
                )
            )

            for _ in range(faltam):
                matricula = str(random.randint(10000000, 99999999))
                while PessoaModel.objects.filter(matricula=matricula).exists():
                    matricula = str(random.randint(10000000, 99999999))

                PessoaModel.objects.create(
                    nome=fake.name(),
                    matricula=matricula,
                    sexo=random.choice(['M', 'F']),
                )
