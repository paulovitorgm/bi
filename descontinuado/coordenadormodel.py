from django.db import models

from apps.pessoas.models import PessoaModel


class CoordenadorModel(models.Model):
    id = models.AutoField(primary_key=True)
    coordenador = models.ForeignKey(
        PessoaModel, on_delete=models.RESTRICT, null=False, blank=False
    )

    class Meta:
        db_table = 'Coordenador'

    def __str__(self):
        return self.coordenador.nome
