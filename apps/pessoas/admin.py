from django.contrib import admin

from .models import PessoaModel, UnidadeDeLotacao


@admin.register(PessoaModel)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'unidade_de_lotacao')

    search_fields = (
        'nome',
        'matricula',
        'unidade_de_lotacao__sigla',
        'unidade_de_lotacao__nome',
    )

    ordering = ('nome',)

    list_per_page = 25


@admin.register(UnidadeDeLotacao)
class UnidadeDeLotacaoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    search_fields = ('sigla', 'nome')
    ordering = ('sigla', 'nome')
