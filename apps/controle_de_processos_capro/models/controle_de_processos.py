from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from apps.controle_de_processos_capro.models.coordenador import CoordenadorModel

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


class ControleDeProcessosModel(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    processo_sei = models.CharField(
        max_length=17,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{17}$',
                message='O processo deve conter exatamente 17 dígitos.',
            )
        ],
        blank=False,
        null=False,
    )
    modalidade = models.CharField(max_length=50, choices=MODALIDADE)
    natureza = models.CharField(max_length=50, choices=NATUREZA)
    abrangencia = models.CharField(max_length=50, choices=ABRANGENCIA)
    forma_de_aprovacao = models.CharField(max_length=50, choices=FORMA_DE_APROVACAO)
    coordenador = models.ForeignKey(CoordenadorModel, on_delete=models.CASCADE)
    custos_indiretos = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )
    esfera_administrativa = models.IntegerField(choices=EsferaAdministrativa.choices)
    ementa = models.TextField(max_length=600)
    mes_da_aprovacao = models.IntegerField(choices=MES)

    class Meta:
        db_table = 'ControleDeProcessos'
        indexes = [
            models.Index(fields=['processo_sei']),
            models.Index(fields=['coordenador']),
            models.Index(fields=['mes_da_aprovacao']),
            models.Index(fields=['esfera_administrativa']),
        ]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(custos_indiretos__gte=0),
                name='custos_indiretos_positivo',
            )
        ]

    @property
    def processo_formatado(self):
        p = self.processo_sei
        return f'{p[:5]}.{p[5:11]}/{p[11:15]}-{p[15:]}'

    def __str__(self):
        return f"""Processo sei: {self.processo_formatado}
                    Ementa: {self.ementa}
                    Coordenador: {self.coordenador}"""
