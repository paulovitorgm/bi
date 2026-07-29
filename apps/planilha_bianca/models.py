from django.db import models

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
)
from apps.entidade.models import EntidadeModel
from apps.pessoas.models import PessoaModel


class PlanilhaModel(models.Model):
    id = models.AutoField(primary_key=True)
    processo_sei = models.OneToOneField(
        ControleDeProcessosModel,
        max_length=17,
        on_delete=models.CASCADE,
        to_field='processo_sei',
        unique=True,
        blank=False,
        null=False,
        related_name='planilha_processo_sei',
        db_index=True
    )
    data_inicio = models.DateField(blank=False, null=False)
    data_termino = models.DateField(blank=False, null=False)
    valor_inicial = models.DecimalField(max_digits=18, decimal_places=2)
    sigla = models.CharField(max_length=20, blank=False, null=False)
    executor = models.ForeignKey(PessoaModel,
                                 on_delete=models.CASCADE,
                                 related_name='planilha_executor',
                                 )
    # coordenador
    supervisor = models.ForeignKey(PessoaModel,
                                   on_delete=models.CASCADE,
                                   related_name='planilha_supervisor')
    # coordenador substituto
    substituto = models.ForeignKey(
        PessoaModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='planilha_substituto',
    )
    relator = models.ForeignKey(
        PessoaModel,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        related_name='planilha_relator',
    )
    entidade = models.ForeignKey(
        EntidadeModel,
        on_delete=models.RESTRICT,
        null=False,
        blank=False,
        related_name='planilha_entidade',
    )
    pste = models.BooleanField(blank=False, null=False)
    participes = models.ManyToManyField(EntidadeModel,
    )


    class Meta:
        db_table = 'Planilha'
        verbose_name = 'Planilha'
        verbose_name_plural = 'Planilhas'

    def __str__(self):
        return self.processo_sei
