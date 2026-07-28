from django.db import models


class CoordenadorModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=180, blank=False, null=False)
    matricula = models.CharField(max_length=18, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'Coordenador'

    def __str__(self):
        return self.nome
