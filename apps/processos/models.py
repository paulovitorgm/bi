from decimal import Decimal

from django.core.validators import RegexValidator
from django.db import models

from apps.pessoas.models import PessoaModel

# ==========================================
# TABELAS DE DOMÍNIO / DIMENSÕES
# ==========================================


class PublicoPrivado(models.TextChoices):
    PUBLICO = 'Publico', 'Publico'
    PRIVADO = 'Privado', 'Privado'


class Onu(models.Model):
    pass


class Unidade(models.Model):
    """Ex: UnB, FUP, FS, DAIA, FT"""

    sigla = models.CharField(max_length=20, unique=True, db_index=True)
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['sigla']

    def __str__(self):
        if self.sigla:
            return f'{self.sigla} - {self.nome}'
        return self.nome


class EntidadeParceira(models.Model):
    """Ex: Finatec, Funape, Convert Consultoria, etc."""

    sigla = models.CharField(max_length=20, unique=True, db_index=True)
    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(
        max_length=20, blank=True, null=True, db_index=True, unique=True
    )
    publico_privado = models.CharField(max_length=15, choices=PublicoPrivado.choices)

    class Meta:
        ordering = ['sigla']
        verbose_name = 'Entidade Parceira'
        verbose_name_plural = 'Entidades Parceiras'

    def __str__(self):
        if self.sigla:
            return f'{self.sigla} - {self.nome}'
        return self.nome


class EsferaAdministrativaChoices(models.TextChoices):
    FEDERAL = 'Federal', 'Federal'
    ESTADUAL = 'Estadual', 'Estadual'
    MUNICIPAL = 'Municipal', 'Municipal'
    INICIATIVA_PRIVADA = 'Iniciativa Privada', 'Iniciativa Privada'
    INTERNACIONAL = 'Internacional', 'Internacional'


class TipoInstrumentoChoices(models.TextChoices):
    CONVENIO = 'Convênio', 'Convênio'
    CONTRATO = 'Contrato', 'Contrato'
    ACORDO_COOPERACAO = 'Acordo de Cooperação', 'Acordo de Cooperação'
    TERMO_COMPROMISSO = 'Termo de Compromisso', 'Termo de Compromisso'
    TERMO_EXECUCAO = (
        'Termo de Execução Descentralizada',
        'Termo de Execução Descentralizada',
    )
    TERMO_OUTORGA = 'Termo de Outorga', 'Termo de Outorga'


class Modalidade(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Natureza(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Abrangencia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class TipoDespesa(models.Model):
    """Ex: Auxílio financeiro a Pesquisador, Serviços de Terceiros PJ, etc."""

    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tipo de Despesa'
        verbose_name_plural = 'Tipos de Despesas'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


# ==========================================
# ENTIDADE PRINCIPAL: PROCESSO / PROJETO
# ==========================================


class ProcessoProjeto(models.Model):
    processo = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text='Apenas números para busca rápida ex: 23106092037202530',
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
    ementa = models.TextField(blank=True, null=True)
    participes_texto = models.TextField(
        blank=True, null=True, help_text='Texto bruto de partícipes se necessário'
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
    # ---------------------------
    # coordenador/executor são iguais?
    # ---------------------------
    # executor = models.ForeignKey(
    #     Pessoa,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='projetos_executados',
    # )
    substituto = models.ForeignKey(
        PessoaModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_substituidos',
    )

    # Financeiros
    # o custo do projeto pode aumentar com o passar do projeto?
    valor_total = models.DecimalField(
        max_digits=25, decimal_places=2, default=Decimal('0.00')
    )
    valor_inicial = models.DecimalField(
        max_digits=25, decimal_places=2, default=Decimal('0.00')
    )
    custos_indiretos = models.DecimalField(
        max_digits=25, decimal_places=2, default=Decimal('0.00')
    )

    # Datas e Prazos (Indexadas para filtros rápidos de período no Power BI)
    dt_inicio = models.DateField(null=True, blank=True, db_index=True)
    dt_termino = models.DateField(null=True, blank=True, db_index=True)
    dt_assinatura = models.DateField(null=True, blank=True)

    # Metadados de Controle Interno / Tramitação
    # tempo_tramitacao = models.CharField(max_length=100, blank=True, null=True)
    forma_aprovacao = models.CharField(max_length=150, blank=True, null=True)
    pste = models.BooleanField(blank=False, null=False, default=False)
    coordenado_por_mulheres = models.BooleanField(default=False)

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


# ==========================================
# PLANO DE APLICAÇÃO DAS DESPESAS (1:N)
# ==========================================


class ItemPlanoDespesa(models.Model):
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
