from django.db import models

from apps.base.models import ModeloAuditavel
from apps.processos.models.processoprojeto import ProcessoProjeto
from apps.processos.models.tipodespesa import TipoDespesa


class ItemPlanoDespesa(ModeloAuditavel):
    processo = models.ForeignKey(
        ProcessoProjeto, on_delete=models.CASCADE, related_name='despesas'
    )
    tipo_despesa = models.ForeignKey(TipoDespesa, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Item do Plano de Despesa'
        verbose_name_plural = 'Itens do Plano de Despesas'

    def __str__(self):
        return f'{self.processo} - {self.tipo_despesa.descricao}: R$ {self.valor}'
