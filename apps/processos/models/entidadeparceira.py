from django.db import models
from processos.models.choices import PublicoPrivado


class EntidadeParceira(models.Model):
    """Ex: Finatec, Funape, Convert Consultoria, etc."""

    sigla = models.CharField(max_length=20, unique=True, db_index=True)
    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(
        max_length=20, blank=True, null=True, db_index=True, unique=True
    )
    publico_privado = models.CharField(max_length=15, choices=PublicoPrivado.choices)

    class Meta:
        ordering = ['sigla']
        verbose_name = 'Entidade Parceira'
        verbose_name_plural = 'Entidades Parceiras'

    def __str__(self):
        if self.sigla:
            return f'{self.sigla} - {self.nome}'
        return self.nome
