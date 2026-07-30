from django.urls import path

from apps.processos.views.modalidade import (
    ModalidadeListView,
    ModalidadeCreateView,
    ModalidadeUpdateView,
    ModalidadeDeleteView,
)

from apps.processos.views.entidade_parceira import (
    EntidadeParceiraCreateView,
    EntidadeParceiraDeleteView,
    EntidadeParceiraListView,
    EntidadeParceiraUpdateView,
)

from apps.processos.views.processos import (
    ProcessoCreateView,
    ProcessoDeleteView,
    ProcessoDetailView,
    ProcessoListView,
    ProcessoUpdateView,
)
from apps.processos.views.unidade import (
    UnidadeCreateView,
    UnidadeDeleteView,
    UnidadeListView,
    UnidadeUpdateView,
)

from apps.processos.views.natureza import (
    NaturezaListView,
    NaturezaCreateView,
    NaturezaUpdateView,
    NaturezaDeleteView,
)

urlpatterns = [
    # Processos
    path('', ProcessoListView.as_view(), name='processo_list'),
    path(
        'novo/',
        ProcessoCreateView.as_view(),
        name='processo_create',
    ),
    path(
        '<int:pk>/',
        ProcessoDetailView.as_view(),
        name='processo_detail',
    ),
    path(
        '<int:pk>/editar/',
        ProcessoUpdateView.as_view(),
        name='processo_update',
    ),
    path(
        '<int:pk>/deletar/',
        ProcessoDeleteView.as_view(),
        name='processo_delete',
    ),
    # # # Domínios # # #
    # Unidades
    path('unidades/', UnidadeListView.as_view(), name='unidade_list'),
    path('unidades/nova/', UnidadeCreateView.as_view(), name='unidade_create'),
    path('unidades/<int:pk>/editar/', UnidadeUpdateView.as_view(), name='unidade_update'),
    path(
        'unidades/<int:pk>/excluir/', UnidadeDeleteView.as_view(), name='unidade_delete'
    ),
    # Entidades Parceiras
    path(
        'entidades-parceiras/',
        EntidadeParceiraListView.as_view(),
        name='entidade_parceira_list',
    ),
    path(
        'entidades-parceiras/nova/',
        EntidadeParceiraCreateView.as_view(),
        name='entidade_parceira_create',
    ),
    path(
        'entidades-parceiras/<int:pk>/editar/',
        EntidadeParceiraUpdateView.as_view(),
        name='entidade_parceira_update',
    ),
    path(
        'entidades-parceiras/<int:pk>/excluir/',
        EntidadeParceiraDeleteView.as_view(),
        name='entidade_parceira_delete',
    ),

    # Modalidade
path(
    'modalidades/',
    ModalidadeListView.as_view(),
    name='modalidade_list'
),

path(
    'modalidades/nova/',
    ModalidadeCreateView.as_view(),
    name='modalidade_create'
),

path(
    'modalidades/<int:pk>/editar/',
    ModalidadeUpdateView.as_view(),
    name='modalidade_update'
),

path(
    'modalidades/<int:pk>/excluir/',
    ModalidadeDeleteView.as_view(),
    name='modalidade_delete'
),

# Natureza

# Natureza
path(
    "natureza/",
    NaturezaListView.as_view(),
    name="natureza_listar",
),
path(
    "natureza/nova/",
    NaturezaCreateView.as_view(),
    name="natureza_create",
),
path(
    "natureza/<int:pk>/editar/",
    NaturezaUpdateView.as_view(),
    name="natureza_update",
),
path(
    "natureza/<int:pk>/excluir/",
    NaturezaDeleteView.as_view(),
    name="natureza_delete",
),


]
# para depois:

# Itens do Plano de Despesa (Atrelados a um processo via URL)
# (
#     path(
#         'processos/<int:processo_pk>/despesas/nova/',
#         ItemPlanoDespesaCreateView.as_view(),
#         name='despesa_create',
#     ),
# )
# (
#     path(
#         'despesas/<int:pk>/editar/',
#         ItemPlanoDespesaUpdateView.as_view(),
#         name='despesa_update',
#     ),
# )
# (
#     path(
#         'despesas/<int:pk>/deletar/',
#         ItemPlanoDespesaDeleteView.as_view(),
#         name='despesa_delete',
#     ),
# )
