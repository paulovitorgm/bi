from django.contrib import admin

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
)

admin.site.register(ControleDeProcessosModel)
