from django.db import models

from apps.base.models import ModeloAuditavel


class TipoInstrumento(ModeloAuditavel):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Tipo de instrumento'
        verbose_name_plural = 'Tipos de instrumento'

    def __str__(self):
        return self.nome
