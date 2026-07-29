from django.urls import path

from apps.pessoas.views import (
    PessoaCreate,
    PessoaDelete,
    PessoaDetail,
    PessoaListView,
    PessoaUpdate,
    buscar_pessoa_para_excluir,
)

urlpatterns = [
    path(
        '',
        PessoaListView.as_view(),
        name='listar-pessoas',
    ),
    path(
        'editar-pessoa/<str:matricula>/',
        PessoaUpdate.as_view(),
        name='editar-pessoa',
    ),
    path(
        'cadastrar-pessoa/',
        PessoaCreate.as_view(),
        name='criar-pessoa',
    ),
    path('pessoas/<str:matricula>/', PessoaDetail.as_view(), name='detalhar-pessoa'),
    path(
        'deletar-pessoa/<str:matricula>/',
        PessoaDelete.as_view(),
        name='confirmar-exclusao-pessoa',
    ),
    path(
        'buscar-pessoa/',
        buscar_pessoa_para_excluir,
        name='buscar-processo',
    ),
]
