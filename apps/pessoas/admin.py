from django.contrib import admin

from .models import PessoaModel


@admin.register(PessoaModel)
class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'matricula',
        'sexo'
    )

    search_fields = (
        'nome',
        'matricula',
        'sexo'
    )

    ordering = ('nome',)

    list_per_page = 25
