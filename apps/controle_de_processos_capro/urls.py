from django.urls import path

from apps.controle_de_processos_capro.views.controle_de_processos import (
    ControleDeProcessosCreate,
    ControleDeProcessosDelete,
    ControleDeProcessosDetail,
    ControleDeProcessosListView,
    ControleDeProcessosUpdate,
    buscar_processo_para_excluir,
)

urlpatterns = [
    # processos
    path(
        'processos/',
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
        'buscar-processo/',
        buscar_processo_para_excluir,
        name='buscar-processo',
    ),
    path(
        'editar-processo/<str:processo_sei>/',
        ControleDeProcessosUpdate.as_view(),
        name='editar-processo',
    ),
    path(
        'deletar-processo/<str:processo_sei>/',
        ControleDeProcessosDelete.as_view(),
        name='confirmar-exclusao-processo',
    ),
]
