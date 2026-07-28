from django.urls import path

from apps.controle_de_processos_capro.views.controle_de_processos import (
    ControleDeProcessosCreate,
    ControleDeProcessosDelete,
    ControleDeProcessosDetail,
    ControleDeProcessosListView,
)
from apps.controle_de_processos_capro.views.coordenador import (
    CoordenadorCreate,
    CoordenadorListView,
)

urlpatterns = [
    path(
        'listar-processos/',
        ControleDeProcessosListView.as_view(),
        name='listar-processos',
    ),
    path(
        'cadastrar-processo/',
        ControleDeProcessosCreate.as_view(),
        name='criar-processo',
    ),
    path(
        'detalhar-processo/<str:processo_sei>/',
        ControleDeProcessosDetail.as_view(),
        name='detalhar-processo',
    ),
    path(
        'deletar-processo/<str:processo_sei>/',
        ControleDeProcessosDelete.as_view(),
        name='deletar-processo',
    ),
    path(
        'listar-coordenadores/',
        CoordenadorListView.as_view(),
        name='listar-coordenadores',
    ),
    path(
        'cadastrar-coordenador/',
        CoordenadorCreate.as_view(),
        name='criar-coordenador',
    ),
]
