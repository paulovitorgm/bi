from django.db import models

from apps.base.models import ModeloAuditavel


class TipoDespesa(ModeloAuditavel):
    """Ex: Auxílio financeiro a Pesquisador, Serviços de Terceiros PJ, etc."""

    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tipo de Despesa'
        verbose_name_plural = 'Tipos de Despesas'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao
