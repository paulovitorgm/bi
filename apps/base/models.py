from django.conf import settings
from django.db import models


class OrigemRegistro(models.TextChoices):
    MANUAL = 'manual', 'Cadastro manual'
    IMPORTACAO = 'importacao', 'Importação'
    INTEGRACAO = 'integracao', 'Integração'


class ModeloAuditavel(models.Model):
    """Metadados comuns para rastreabilidade e atualização incremental."""

    criado_em = models.DateTimeField(auto_now_add=True, db_index=True)
    atualizado_em = models.DateTimeField(auto_now=True, db_index=True)
    origem_registro = models.CharField(
        max_length=20,
        choices=OrigemRegistro.choices,
        default=OrigemRegistro.MANUAL,
    )
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_criados',
    )
    atualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_atualizados',
    )

    class Meta:
        abstract = True
