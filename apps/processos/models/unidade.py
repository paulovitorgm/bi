from django.db import models


class Unidade(models.Model):
    """Ex: UnB, FUP, FS, DAIA, FT"""

    sigla = models.CharField(max_length=20, unique=True, db_index=True)
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['sigla']

    def __str__(self):
        if self.sigla:
            return f'{self.sigla} - {self.nome}'
        return self.nome
