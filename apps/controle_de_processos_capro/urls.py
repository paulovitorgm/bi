from django.urls import path

from apps.controle_de_processos_capro.views import (
    ControleDeProcessosListView,
    ControleDeProcessosCreate)

urlpatterns = [
    path('listar/', ControleDeProcessosListView.as_view(), name='listar'),
    path('cadastrar/', ControleDeProcessosCreate.as_view(), name='criar')
]
