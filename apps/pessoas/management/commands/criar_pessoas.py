import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.pessoas.models import PessoaModel

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Cria pessoas (coordenadores) fictícias em lote.'

    def add_arguments(self, parser):  # ruff: ignore[no-self-use]
        parser.add_argument(
            'quantidade', type=int, help='Quantidade de pessoas a serem criadas.'
        )

    def handle(self, *args, **options):
        quantidade = options['quantidade']
        pessoas = []

        for _ in range(quantidade):
            matricula = str(random.randint(10000000, 99999999))
            while PessoaModel.objects.filter(matricula=matricula).exists():
                matricula = str(random.randint(10000000, 99999999))

            pessoas.append(
                PessoaModel(
                    nome=fake.name(),
                    matricula=matricula,
                    sexo=random.choice(['M', 'F']),
                )
            )

        if pessoas:
            print(
                f'Exemplo gerado -> Nome: '
                f'{pessoas[0].nome} | '
                f'Matrícula: {pessoas[0].matricula} |'
                f' Sexo: {pessoas[0].sexo}'
            )

            PessoaModel.objects.bulk_create(pessoas)

        self.stdout.write(
            self.style.SUCCESS(f'{quantidade} pessoas criadas com sucesso!')
        )
