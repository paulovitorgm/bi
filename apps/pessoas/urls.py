from django.urls import path

from apps.pessoas.views import (
    PessoaCreate,
    PessoaDelete,
    PessoaListView,
    PessoaUpdate,
    UnidadeDeLotacaoModalCreateView,
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
    path(
        'modal/unidades-de-lotacao/',
        UnidadeDeLotacaoModalCreateView.as_view(),
        name='modal_unidade_lotacao_criar',
    ),
    path(
        'deletar-pessoa/<str:matricula>/',
        PessoaDelete.as_view(),
        name='confirmar-exclusao-pessoa',
    ),
]
