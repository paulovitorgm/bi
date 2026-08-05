from django.db import models

from apps.base.models import ModeloAuditavel


class Abrangencia(ModeloAuditavel):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
