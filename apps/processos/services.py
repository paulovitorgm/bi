"""Serviços para operações em lote de processos."""

from decimal import Decimal

from django.db.models import Sum
from django.utils import timezone

from apps.processos.models.processoprojeto import ProcessoProjeto
from apps.processos.models.termosadtivos import TermosAdtivos


def recalcular_valores_totais(processo_ids):
    """Recalcula os totais dos processos afetados por uma carga em massa.

    Use após ``bulk_create()``, ``bulk_update()`` ou ``QuerySet.update()`` em
    termos aditivos. Essas operações não executam ``save()`` e, portanto, não
    acionam o cálculo automático do modelo.
    """
    ids = {processo_id for processo_id in processo_ids if processo_id is not None}
    if not ids:
        return 0

    totais_aditivos = {
        item['processo_id']: item['total']
        for item in TermosAdtivos.objects
        .filter(processo_id__in=ids)
        .values('processo_id')
        .annotate(total=Sum('valor'))
    }
    processos = list(ProcessoProjeto.objects.filter(pk__in=ids))
    atualizado_em = timezone.now()
    for processo in processos:
        processo.valor_total = processo.valor_inicial + totais_aditivos.get(
            processo.pk, Decimal('0.00')
        )
        processo.atualizado_em = atualizado_em

    ProcessoProjeto.objects.bulk_update(processos, ['valor_total', 'atualizado_em'])
    return len(processos)
