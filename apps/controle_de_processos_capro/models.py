from django.db import models

NATUREZA = [("", ""), ("", ""), ("", "")]
MODALIDADE = [("", ""), ("", ""), ("", "")]
ABRANGENCIA = [("", ""), ("", ""), ("", "")]
FORMA_DE_APROVACAO = [("", ""), ("", ""), ("", "")]
ESFERA_ADM = [(1, "Federal"), (2, "Estadual"), (3, "Municipal"),
    (4, "Iniciativa privada"), (5, "Internacional")]
MES = [(1, "Janeiro"), (2, "Fevereiro"), (3, "Março"), (4, "Abril"),
       (5, "Maio"), (6, "Junho"), (7, "Julho"), (8, "Agosto"),
       (9, "Setembro"), (10, "Outubro"), (11, "Novembro"), (12, "Dezembro")]


class Coordenador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=180, blank=False, null=False)
    matricula = models.CharField(max_length=18, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'Coordenador'


class ControleDeProcessosModel(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    processo_sei = models.CharField(max_length=17)
    modalidade = models.CharField(max_length=50, choices=MODALIDADE)
    natureza = models.CharField(max_length=50, choices=NATUREZA)
    abrangencia = models.CharField(max_length=50, choices=ABRANGENCIA)
    forma_de_aprovacao = models.CharField(max_length=50, choices=FORMA_DE_APROVACAO)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)
    custos_indiretos = models.FloatField()
    esfera_administrativa = models.IntegerField(choices=ESFERA_ADM)
    ementa = models.TextField(max_length=600)
    mes_da_aprovacao = models.IntegerField(choices=MES)

    class Meta:
        db_table = 'ControleDeProcessos'

