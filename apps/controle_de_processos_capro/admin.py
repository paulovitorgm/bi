from django.contrib import admin

from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
)
from apps.controle_de_processos_capro.models.coordenador import CoordenadorModel

admin.site.register(CoordenadorModel)
admin.site.register(ControleDeProcessosModel)
