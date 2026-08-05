from django.db import models


class ParticipesModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=30, unique=True, db_index=True)

    class Meta:
        ordering = ['sigla']
        verbose_name = 'Participe'
        verbose_name_plural = 'Participes'

    def __str__(self):
        return f'{self.sigla} - {self.nome}'
