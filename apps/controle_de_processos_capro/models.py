from django.db import models

NATUREZA = [('', ''), ('', ''), ('', '')]
MODALIDADE = [('', ''), ('', ''), ('', '')]
ABRANGENCIA = [('', ''), ('', ''), ('', '')]
FORMA_DE_APROVACAO = [('', ''), ('', ''), ('', '')]
MES = [
    (1, 'Janeiro'),
    (2, 'Fevereiro'),
    (3, 'Março'),
    (4, 'Abril'),
    (5, 'Maio'),
    (6, 'Junho'),
    (7, 'Julho'),
    (8, 'Agosto'),
    (9, 'Setembro'),
    (10, 'Outubro'),
    (11, 'Novembro'),
    (12, 'Dezembro'),
]


class EsferaAdministrativa(models.IntegerChoices):
    FEDERAL = 1, 'Federal'
    ESTADUAL = 2, 'Estadual'
    MUNICIPAL = 3, 'Municipal'
    PRIVADA = 4, 'Iniciativa Privada'
    INTERNACIONAL = 5, 'Internacional'

    def __str__(self):
        return self.value


class CoordenadorModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=180, blank=False, null=False)
    matricula = models.CharField(max_length=18, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'Coordenador'

    def __str__(self):
        return self.nome
