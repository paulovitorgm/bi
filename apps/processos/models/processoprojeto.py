from decimal import Decimal

from django.core.validators import RegexValidator
from django.db import models

from apps.pessoas.models import PessoaModel, SexoChoices
from apps.processos.models.abrangencia import Abrangencia
from apps.processos.models.choices import (
    EsferaAdministrativaChoices,
    OdsOnuChoices,
    TipoInstrumentoChoices,
)
from apps.processos.models.entidadeparceira import EntidadeParceira
from apps.processos.models.modalidade import Modalidade
from apps.processos.models.natureza import Natureza
from apps.processos.models.participesmodel import ParticipesModel
from apps.processos.models.termosadtivos import TermosAdtivos
from apps.processos.models.unidade import Unidade


class ProcessoProjeto(models.Model):
    processo = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text='Apenas números para busca rápida ex: 2310600000000001',
        validators=[
            RegexValidator(
                regex=r'^\d+$', message='O processo deve conter apenas números.'
            )
        ],
    )
    numero_convenio = models.CharField(
        max_length=50, blank=True, null=True, db_index=True
    )
    # Detalhes
    nome_do_processo = models.CharField(max_length=255, blank=False, null=False)
    ementa = models.TextField(blank=True, null=True)
    participes = models.ManyToManyField(
        ParticipesModel, blank=True, related_name='processos'
    )
    # Chaves Estrangeiras de Domínio
    unidade_interessada = models.ManyToManyField(
        Unidade,
        related_name='projetos',
    )
    tipo_instrumento = models.CharField(
        max_length=50, choices=TipoInstrumentoChoices.choices
    )
    modalidade = models.ManyToManyField(Modalidade, related_name='processos')
    esfera_administrativa = models.CharField(
        max_length=30, choices=EsferaAdministrativaChoices.choices
    )
    natureza = models.ManyToManyField(Natureza, related_name='processos', blank=True)
    # na planilha tem apenas Nacional, Internacional, Não se aplica e Vazio
    abrangencia = models.ForeignKey(
        Abrangencia, on_delete=models.SET_NULL, null=True, blank=True
    )
    entidade_parceira = models.ForeignKey(
        EntidadeParceira, on_delete=models.SET_NULL, null=True, blank=True
    )
    # Nome Executor / coordenador
    coordenador = models.ForeignKey(
        PessoaModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_coordenados',
    )
    supervisor_academico = models.ForeignKey(
        PessoaModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_supervisionados',
    )
    relator = models.ForeignKey(
        PessoaModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_relatados',
    )

    substituto = models.ForeignKey(
        PessoaModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_substituidos',
    )

    # Financeiros
    valor_total = models.DecimalField(
        max_digits=25, decimal_places=2, default=Decimal('0.00')
    )
    # valor_inicial = models.DecimalField(
    #     max_digits=25, decimal_places=2, default=Decimal('0.00')
    # )
    custos_indiretos = models.DecimalField(
        max_digits=25, decimal_places=2, default=Decimal('0.00')
    )

    # Datas e Prazos (Indexadas para filtros rápidos de período no Power BI)
    dt_inicio = models.DateField(null=True, blank=True, db_index=True)
    dt_termino = models.DateField(null=True, blank=True, db_index=True)
    dt_assinatura = models.DateField(null=True, blank=True)

    # Metadados de Controle Interno / Tramitação
    ods_onu = models.CharField(max_length=50, choices=OdsOnuChoices.choices, blank=True)
    termo_adtivo = models.ManyToManyField(
        TermosAdtivos,
        blank=False,
        null=False,
        related_name='termos_adtivos',
    )

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'
        indexes = [
            models.Index(fields=['dt_inicio']),
            models.Index(fields=['dt_termino']),
            models.Index(fields=['processo']),
            models.Index(fields=['entidade_parceira']),
        ]

    def __str__(self):
        return f'SEI nº: {self.processo}'

    def save(self, *args, **kwargs):
        self.coordenado_por_mulheres = (
            self.coordenador is not None and self.coordenador.sexo == SexoChoices.FEM
        )
        super().save(*args, **kwargs)
