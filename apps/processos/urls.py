from django.urls import path

from apps.processos.views.cadastros import (
    AbrangenciaCreateView, AbrangenciaDeleteView, AbrangenciaListView, AbrangenciaUpdateView,
    ParticipeCreateView, ParticipeDeleteView, ParticipeListView, ParticipeUpdateView,
    TipoDespesaCreateView, TipoDespesaDeleteView, TipoDespesaListView, TipoDespesaUpdateView,
    TipoInstrumentoCreateView, TipoInstrumentoDeleteView, TipoInstrumentoListView, TipoInstrumentoUpdateView,
)
from apps.processos.views.modais import (
    AbrangenciaModalCreateView, EntidadeModalCreateView, ModalidadeModalCreateView,
    NaturezaModalCreateView, ParticipeModalCreateView, PessoaModalCreateView,
    TipoInstrumentoModalCreateView, UnidadeModalCreateView,
)

from apps.processos.views.entidade_parceira import (
    EntidadeParceiraCreateView,
    EntidadeParceiraDeleteView,
    EntidadeParceiraListView,
    EntidadeParceiraUpdateView,
)
from apps.processos.views.modalidade import (
    ModalidadeCreateView,
    ModalidadeDeleteView,
    ModalidadeListView,
    ModalidadeUpdateView,
)
from apps.processos.views.natureza import (
    NaturezaCreateView,
    NaturezaDeleteView,
    NaturezaListView,
    NaturezaUpdateView,
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

urlpatterns = [
    path('modal/unidades/', UnidadeModalCreateView.as_view(), name='modal_unidade_criar'),
    path('modal/participes/', ParticipeModalCreateView.as_view(), name='modal_participe_criar'),
    path('modal/modalidades/', ModalidadeModalCreateView.as_view(), name='modal_modalidade_criar'),
    path('modal/naturezas/', NaturezaModalCreateView.as_view(), name='modal_natureza_criar'),
    path('modal/abrangencias/', AbrangenciaModalCreateView.as_view(), name='modal_abrangencia_criar'),
    path('modal/entidades/', EntidadeModalCreateView.as_view(), name='modal_entidade_criar'),
    path('modal/tipos-instrumento/', TipoInstrumentoModalCreateView.as_view(), name='modal_tipo_instrumento_criar'),
    path('modal/pessoas/', PessoaModalCreateView.as_view(), name='modal_pessoa_criar'),
    # Processos
    path(
        '',
        ProcessoListView.as_view(),
        name='processo_listar',
    ),
    path(
        'novo/',
        ProcessoCreateView.as_view(),
        name='processo_criar',
    ),
    path(
        '<str:processo>/detalhar/',
        ProcessoDetailView.as_view(),
        name='processo_detalhar',
    ),
    path(
        '<str:processo>/editar/',
        ProcessoUpdateView.as_view(),
        name='processo_editar',
    ),
    path(
        '<str:processo>/excluir/',
        ProcessoDeleteView.as_view(),
        name='processo_deletar',
    ),
    # # # Domínios # # #
    # Unidades
    path('unidades/', UnidadeListView.as_view(), name='unidade_listar'),
    path('unidades/nova/', UnidadeCreateView.as_view(), name='unidade_criar'),
    path('unidades/<int:pk>/editar/', UnidadeUpdateView.as_view(), name='unidade_editar'),
    path(
        'unidades/<int:pk>/excluir/', UnidadeDeleteView.as_view(), name='unidade_delete'
    ),
    # Entidades Parceiras
    path(
        'entidades-parceiras/',
        EntidadeParceiraListView.as_view(),
        name='entidade_parceira_listar',
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
    path('modalidades/', ModalidadeListView.as_view(), name='modalidade_listar'),
    path('modalidades/nova/', ModalidadeCreateView.as_view(), name='modalidade_create'),
    path(
        'modalidades/<int:pk>/editar/',
        ModalidadeUpdateView.as_view(),
        name='modalidade_update',
    ),
    path(
        'modalidades/<int:pk>/excluir/',
        ModalidadeDeleteView.as_view(),
        name='modalidade_delete',
    ),
    # Natureza
    # Natureza
    path(
        'natureza/',
        NaturezaListView.as_view(),
        name='natureza_listar',
    ),
    path(
        'natureza/nova/',
        NaturezaCreateView.as_view(),
        name='natureza_create',
    ),
    path(
        'natureza/<int:pk>/editar/',
        NaturezaUpdateView.as_view(),
        name='natureza_update',
    ),
    path(
        'natureza/<int:pk>/excluir/',
        NaturezaDeleteView.as_view(),
        name='natureza_delete',
    ),
    path('abrangencias/', AbrangenciaListView.as_view(), name='abrangencia_listar'),
    path('abrangencias/nova/', AbrangenciaCreateView.as_view(), name='abrangencia_criar'),
    path('abrangencias/<int:pk>/editar/', AbrangenciaUpdateView.as_view(), name='abrangencia_editar'),
    path('abrangencias/<int:pk>/excluir/', AbrangenciaDeleteView.as_view(), name='abrangencia_excluir'),
    path('participes/', ParticipeListView.as_view(), name='participe_listar'),
    path('participes/novo/', ParticipeCreateView.as_view(), name='participe_criar'),
    path('participes/<int:pk>/editar/', ParticipeUpdateView.as_view(), name='participe_editar'),
    path('participes/<int:pk>/excluir/', ParticipeDeleteView.as_view(), name='participe_excluir'),
    path('tipos-despesa/', TipoDespesaListView.as_view(), name='tipo_despesa_listar'),
    path('tipos-despesa/novo/', TipoDespesaCreateView.as_view(), name='tipo_despesa_criar'),
    path('tipos-despesa/<int:pk>/editar/', TipoDespesaUpdateView.as_view(), name='tipo_despesa_editar'),
    path('tipos-despesa/<int:pk>/excluir/', TipoDespesaDeleteView.as_view(), name='tipo_despesa_excluir'),
    path('tipos-instrumento/', TipoInstrumentoListView.as_view(), name='tipo_instrumento_listar'),
    path('tipos-instrumento/novo/', TipoInstrumentoCreateView.as_view(), name='tipo_instrumento_criar'),
    path('tipos-instrumento/<int:pk>/editar/', TipoInstrumentoUpdateView.as_view(), name='tipo_instrumento_editar'),
    path('tipos-instrumento/<int:pk>/excluir/', TipoInstrumentoDeleteView.as_view(), name='tipo_instrumento_excluir'),
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
