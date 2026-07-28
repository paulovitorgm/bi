from django.urls import path

from apps.controle_de_processos_capro.views import (
    ControleDeProcessosCreate,
    ControleDeProcessosListView, CoordenadorCreate, CoordenadorListView,
)

urlpatterns = [
    path('listar-processos/', ControleDeProcessosListView.as_view(), name='listar'),
    path('cadastrar-processo/', ControleDeProcessosCreate.as_view(), name='criar-processo'),
    path('cadastrar-coordenador/', CoordenadorCreate.as_view(), name='criar-coordenador'),
    path('listar-coordenadores/', CoordenadorListView.as_view(), name='listar-coordenadores'),
]
