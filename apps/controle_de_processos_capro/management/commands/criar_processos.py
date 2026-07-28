# ruff: noqa: PLR6301
import random
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
    EsferaAdministrativa,
)
from apps.controle_de_processos_capro.models.coordenador import CoordenadorModel

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Cria processos fictícios.'

    def add_arguments(self, parser):
        parser.add_argument('quantidade', type=int, help='Quantidade de processos.')

    def handle(self, *args, **options):
        quantidade = options['quantidade']

        coordenadores = self._obter_coordenadores()

        processos = []

        for _ in range(quantidade):
            processos.append(
                ControleDeProcessosModel(
                    processo_sei=fake.unique.numerify('#################'),
                    modalidade=random.randint(1, 3),
                    natureza=random.randint(1, 4),
                    abrangencia=random.randint(1, 3),
                    forma_de_aprovacao=random.randint(1, 3),
                    coordenador=random.choice(coordenadores),
                    custos_indiretos=Decimal(f'{random.uniform(0, 50000):.2f}'),
                    esfera_administrativa=random.choice(EsferaAdministrativa.values),
                    ementa=fake.sentence(nb_words=8),
                    mes_da_aprovacao=random.randint(1, 12),
                )
            )
        print(processos[0])
        print(processos[0].__dict__)
        ControleDeProcessosModel.objects.bulk_create(processos)

        self.stdout.write(self.style.SUCCESS(f'{quantidade} processos criados.'))

    def _obter_coordenadores(self):
        coordenadores = list(CoordenadorModel.objects.all())

        if not coordenadores:
            raise CommandError('Nenhum coordenador cadastrado.')

        return coordenadores

    def _gerar_processos(self, quantidade, coordenadores):
        processos = []

        for _ in range(quantidade):
            processos.append(ControleDeProcessosModel(...))

        return processos
