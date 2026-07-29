from django.db import models
import re


# ==========================================
# TABELAS DE DOMÍNIO / DIMENSÕES
# ==========================================


class Unidade(models.Model):
    """Ex: UnB, FUP, FS, DAIA, FT"""

    sigla = models.CharField(max_length=20, unique=True, db_index=True)
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return self.sigla


class EntidadeParceira(models.Model):
    """Ex: Finatec, Funape, Convert Consultoria, etc."""

    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'Entidade Parceira'
        verbose_name_plural = 'Entidades Parceiras'

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    """Cadastro único de Pessoas (Coordenadores, Supervisores, Relatores, Executores)"""

    nome = models.CharField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome


class TipoInstrumento(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome


class EsferaAdministrativa(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Natureza(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Abrangencia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class TipoDespesa(models.Model):
    """Ex: Auxílio financeiro a Pesquisador, Serviços de Terceiros PJ, etc."""

    descricao = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Tipo de Despesa'
        verbose_name_plural = 'Tipos de Despesas'

    def __str__(self):
        return self.descricao


# ==========================================
# ENTIDADE PRINCIPAL: PROCESSO / PROJETO
# ==========================================


class ProcessoProjeto(models.Model):
    # Identificadores do Processo
    numero_processo_limpo = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        help_text='Apenas números para busca rápida ex: 23106092037202530',
    )
    numero_processo_formatado = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        help_text='Formatado ex: 23106.092037/2025-30',
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
    unidade_interessada = models.ForeignKey(
        Unidade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_interessados',
    )
    tipo_instrumento = models.ForeignKey(
        TipoInstrumento, on_delete=models.SET_NULL, null=True, blank=True
    )
    modalidade = models.ForeignKey(
        Modalidade, on_delete=models.SET_NULL, null=True, blank=True
    )
    esfera_administrativa = models.ForeignKey(
        EsferaAdministrativa, on_delete=models.SET_NULL, null=True, blank=True
    )
    natureza = models.ForeignKey(
        Natureza, on_delete=models.SET_NULL, null=True, blank=True
    )
    abrangencia = models.ForeignKey(
        Abrangencia, on_delete=models.SET_NULL, null=True, blank=True
    )
    entidade_parceira = models.ForeignKey(
        EntidadeParceira, on_delete=models.SET_NULL, null=True, blank=True
    )

    # Relacionamentos com Pessoas (FKs diretas garantem alta performance em consultas)
    coordenador = models.ForeignKey(
        Pessoa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_coordenados',
    )
    supervisor_academico = models.ForeignKey(
        Pessoa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_supervisionados',
    )
    relator = models.ForeignKey(
        Pessoa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_relatados',
    )
    executor = models.ForeignKey(
        Pessoa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_executados',
    )
    substituto = models.ForeignKey(
        Pessoa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_substituidos',
    )

    # Valores Financeiros
    valor_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    valor_inicial = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    custos_indiretos = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    # Datas e Prazos (Indexadas para filtros rápidos de período no Power BI)
    dt_inicio = models.DateField(null=True, blank=True, db_index=True)
    dt_termino = models.DateField(null=True, blank=True, db_index=True)
    dt_assinatura = models.DateField(null=True, blank=True)

    # Metadados de Controle Interno / Tramitação
    tempo_tramitacao = models.CharField(max_length=100, blank=True, null=True)
    aprovacao = models.CharField(max_length=150, blank=True, null=True)
    mes_aprovacao = models.CharField(max_length=50, blank=True, null=True)
    ano_aprovacao = models.IntegerField(null=True, blank=True, db_index=True)
    pste = models.CharField(max_length=100, blank=True, null=True)
    coordenado_por_mulheres = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Processo / Projeto'
        verbose_name_plural = 'Processos / Projetos'

    def clean_process_number(self, value):
        """Método auxiliar para remover caracteres especiais do número do processo"""
        if value:
            return re.sub(r'\D', '', str(value))
        return ''

    def save(self, *args, **kwargs):
        if not self.numero_processo_limpo and self.numero_processo_formatado:
            self.numero_processo_limpo = self.clean_process_number(
                self.numero_processo_formatado
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.numero_processo_formatado or self.numero_processo_limpo}'


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
