from django.contrib import admin

from .models import PessoaModel


@admin.register(PessoaModel)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'unidade_de_lotacao')

    search_fields = ('nome', 'matricula', 'unidade_de_lotacao')

    ordering = ('nome',)

    list_per_page = 25
