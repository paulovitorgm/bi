from decimal import Decimal

from django.db import models

from apps.base.models import ModeloAuditavel


class TermosAdtivos(ModeloAuditavel):
    processo = models.ForeignKey(
        'processos.ProcessoProjeto',
        on_delete=models.CASCADE,
        related_name='termos_aditivos',
    )
    termo = models.CharField(max_length=100, unique=True)
    dt_termino = models.DateField(null=True, blank=True, db_index=True)
    dt_assinatura = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=25, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        verbose_name = 'Termo de Adtivos'
        verbose_name_plural = 'Termos de Adtivos'
        ordering = ['dt_termino']

    def __str__(self):
        return self.termo
