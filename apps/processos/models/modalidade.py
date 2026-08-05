from django.db import models

from apps.base.models import ModeloAuditavel


class Modalidade(ModeloAuditavel):
    nome = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
