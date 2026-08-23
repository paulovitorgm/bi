import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.pessoas.models import PessoaModel, UnidadeDeLotacao

fake = Faker('pt_BR')


class Command(BaseCommand):
    help = 'Cria pessoas fictícias em lote.'

    def add_arguments(self, parser):  # ruff: ignore[no-self-use]
        parser.add_argument(
            'quantidade',
            type=int,
            help='Quantidade de pessoas a serem criadas.',
        )

    def handle(self, *args, **options):
        quantidade = options['quantidade']
        if quantidade < 0:
            self.stderr.write(self.style.ERROR('A quantidade não pode ser negativa.'))
            return

        unidades = list(UnidadeDeLotacao.objects.all())
        matriculas_existentes = set(
            PessoaModel.objects.values_list('matricula', flat=True)
        )
        pessoas = []
        proxima_matricula = random.randint(10000000, 99999999)

        while len(pessoas) < quantidade:
            matricula = str(proxima_matricula)
            proxima_matricula += 1
            if matricula in matriculas_existentes:
                continue
            matriculas_existentes.add(matricula)
            pessoas.append(
                PessoaModel(
                    nome=fake.name(),
                    matricula=matricula,
                    unidade_de_lotacao=random.choice(unidades) if unidades else None,
                )
            )

        if pessoas:
            PessoaModel.objects.bulk_create(pessoas, batch_size=1000)

        self.stdout.write(
            self.style.SUCCESS(f'{quantidade} pessoas criadas com sucesso!')
        )
