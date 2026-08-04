from django.contrib import admin

from .models import (
    Abrangencia,
    EntidadeParceira,
    ItemPlanoDespesa,
    Modalidade,
    Natureza,
    ProcessoProjeto,
    TipoDespesa,
    Unidade,
)


list_display = (
    'processo',
    'numero_convenio',
    'nome_do_processo',
    'ementa',
    'participes',
    'unidade_interessada',
    'tipo_instrumento',
    'modalidade',
    'esfera_administrativa',
    'natureza',
    'abrangencia',
    'entidade_parceira',
    'coordenador',
    'supervisor_academico',
    'relator',
    'substituto',
    'valor_total',
    'valor_inicial',
    'custos_indiretos',
    'dt_inicio',
    'dt_termino',
    'dt_assinatura',
    'forma_aprovacao',
    'ods_onu',
    'pste',
)
@admin.register(ProcessoProjeto)
class ProcessoProjetoAdmin(admin.ModelAdmin):

    search_fields = (
        'processo',
        'nome_do_processo',
        'ementa',
        'entidade_parceira__nome',
    )

    list_filter = (
        'tipo_instrumento',
        'esfera_administrativa',
        'forma_aprovacao',
        'dt_inicio',
        'dt_termino',
        'pste',
    )

    autocomplete_fields = (
        'coordenador',
        'supervisor_academico',
        'relator',
        'substituto',
        'entidade_parceira',
    )

    list_select_related = (
        'coordenador',
        'supervisor_academico',
        'relator',
        'substituto',
        'entidade_parceira',
    )

    ordering = ('-dt_inicio',)

    list_per_page = 25


@admin.register(EntidadeParceira)
class EntidadeParceiraAdmin(admin.ModelAdmin):
    list_display = (
        'sigla',
        'nome',
        'cnpj_cpf',
        'publico_privado'
    )

    search_fields = (
        'sigla',
        'nome',
        'cnpj_cpf',
        'publico_privado'
    )

    list_filter = ('publico_privado', 'sigla')

    ordering = ('sigla', 'nome')


@admin.register(Natureza)
class NaturezaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    search_fields = ('nome',)

    ordering = ('nome',)


@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = (
        'sigla',
        'nome',
    )

    search_fields = (
        'sigla',
        'nome',
    )

    ordering = ('sigla',)


@admin.register(Abrangencia)
class AbrangenciaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    search_fields = ('nome',)

    ordering = ('nome',)


@admin.register(TipoDespesa)
class TipoDespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)

    search_fields = ('descricao',)

    ordering = ('descricao',)


@admin.register(ItemPlanoDespesa)
class ItemPlanoDespesaAdmin(admin.ModelAdmin):
    list_display = (
        'processo',
        'tipo_despesa',
        'valor'
    )

    search_fields = ('tipo_despesa',)

    autocomplete_fields = ('tipo_despesa',)

    ordering = ('tipo_despesa',)
