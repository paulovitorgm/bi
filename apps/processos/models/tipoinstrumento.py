from django.db import models

from apps.base.models import ModeloAuditavel


class TipoInstrumento(ModeloAuditavel):
    nome = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome
