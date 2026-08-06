from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.base.mixins import AuditoriaUsuarioMixin, PaginacaoMixin
from apps.processos.forms.cadastrosform import (
    AbrangenciaForm,
    ParticipeForm,
    TermoAditivoForm,
    TipoInstrumentoForm,
)
from apps.processos.forms.tipodespesaform import TipoDespesaForm
from apps.processos.models.abrangencia import Abrangencia
from apps.processos.models.participesmodel import ParticipesModel
from apps.processos.models.termosadtivos import TermosAdtivos
from apps.processos.models.tipodespesa import TipoDespesa
from apps.processos.models.tipoinstrumento import TipoInstrumento


class CadastroListView(PaginacaoMixin, ListView):
    template_name = 'processos/cadastros/listar.html'
    context_object_name = 'objetos'
    paginate_by = 20
    titulo = ''
    criar_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'titulo': self.titulo, 'criar_url': self.criar_url})
        return context


class CadastroCreateView(AuditoriaUsuarioMixin, CreateView):
    template_name = 'processos/cadastros/form.html'
    titulo = ''
    listar_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'titulo': self.titulo, 'listar_url': self.listar_url})
        return context


class CadastroUpdateView(AuditoriaUsuarioMixin, UpdateView):
    template_name = 'processos/cadastros/form.html'
    titulo = ''
    listar_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'titulo': self.titulo, 'listar_url': self.listar_url})
        return context


class CadastroDeleteView(DeleteView):
    template_name = 'processos/cadastros/deletar.html'
    titulo = ''
    listar_url = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'titulo': self.titulo, 'listar_url': self.listar_url})
        return context


class AbrangenciaListView(CadastroListView):
    model, titulo, criar_url = Abrangencia, 'Abrangências', 'abrangencia_criar'


class AbrangenciaCreateView(CadastroCreateView):
    model, form_class, titulo = Abrangencia, AbrangenciaForm, 'Nova abrangência'
    success_url, listar_url = reverse_lazy('abrangencia_listar'), 'abrangencia_listar'


class AbrangenciaUpdateView(CadastroUpdateView):
    model, form_class, titulo = Abrangencia, AbrangenciaForm, 'Editar abrangência'
    success_url, listar_url = reverse_lazy('abrangencia_listar'), 'abrangencia_listar'


class AbrangenciaDeleteView(CadastroDeleteView):
    model, titulo = Abrangencia, 'Excluir abrangência'
    success_url, listar_url = reverse_lazy('abrangencia_listar'), 'abrangencia_listar'


class ParticipeListView(CadastroListView):
    model, titulo, criar_url = ParticipesModel, 'Partícipes', 'participe_criar'


class ParticipeCreateView(CadastroCreateView):
    model, form_class, titulo = ParticipesModel, ParticipeForm, 'Novo partícipe'
    success_url, listar_url = reverse_lazy('participe_listar'), 'participe_listar'


class ParticipeUpdateView(CadastroUpdateView):
    model, form_class, titulo = ParticipesModel, ParticipeForm, 'Editar partícipe'
    success_url, listar_url = reverse_lazy('participe_listar'), 'participe_listar'


class ParticipeDeleteView(CadastroDeleteView):
    model, titulo = ParticipesModel, 'Excluir partícipe'
    success_url, listar_url = reverse_lazy('participe_listar'), 'participe_listar'


class TipoDespesaListView(CadastroListView):
    model, titulo, criar_url = (TipoDespesa, 'Tipos de despesa', 'tipo_despesa_criar')


class TipoDespesaCreateView(CadastroCreateView):
    model, form_class, titulo = TipoDespesa, TipoDespesaForm, 'Novo tipo de despesa'
    success_url, listar_url = (reverse_lazy('tipo_despesa_listar'), 'tipo_despesa_listar')


class TipoDespesaUpdateView(CadastroUpdateView):
    model, form_class, titulo = TipoDespesa, TipoDespesaForm, 'Editar tipo de despesa'
    success_url, listar_url = (reverse_lazy('tipo_despesa_listar'), 'tipo_despesa_listar')


class TipoDespesaDeleteView(CadastroDeleteView):
    model, titulo = TipoDespesa, 'Excluir tipo de despesa'
    success_url, listar_url = (reverse_lazy('tipo_despesa_listar'), 'tipo_despesa_listar')


class TipoInstrumentoListView(CadastroListView):
    model, titulo, criar_url = (
        TipoInstrumento,
        'Tipos de instrumento',
        'tipo_instrumento_criar',
    )


class TipoInstrumentoCreateView(CadastroCreateView):
    model, form_class, titulo = (
        TipoInstrumento,
        TipoInstrumentoForm,
        'Novo tipo de instrumento',
    )
    success_url, listar_url = (
        reverse_lazy('tipo_instrumento_listar'),
        'tipo_instrumento_listar',
    )


class TipoInstrumentoUpdateView(CadastroUpdateView):
    model, form_class, titulo = (
        TipoInstrumento,
        TipoInstrumentoForm,
        'Editar tipo de instrumento',
    )
    success_url, listar_url = (
        reverse_lazy('tipo_instrumento_listar'),
        'tipo_instrumento_listar',
    )


class TipoInstrumentoDeleteView(CadastroDeleteView):
    model, titulo = TipoInstrumento, 'Excluir tipo de instrumento'
    success_url, listar_url = (
        reverse_lazy('tipo_instrumento_listar'),
        'tipo_instrumento_listar',
    )


class TermoAditivoListView(CadastroListView):
    model, titulo, criar_url = TermosAdtivos, 'Termos aditivos', 'termo_aditivo_criar'


class TermoAditivoCreateView(CadastroCreateView):
    model, form_class, titulo = TermosAdtivos, TermoAditivoForm, 'Novo termo aditivo'
    success_url, listar_url = reverse_lazy('termo_aditivo_listar'), 'termo_aditivo_listar'


class TermoAditivoUpdateView(CadastroUpdateView):
    model, form_class, titulo = TermosAdtivos, TermoAditivoForm, 'Editar termo aditivo'
    success_url, listar_url = reverse_lazy('termo_aditivo_listar'), 'termo_aditivo_listar'


class TermoAditivoDeleteView(CadastroDeleteView):
    model, titulo = TermosAdtivos, 'Excluir termo aditivo'
    success_url, listar_url = reverse_lazy('termo_aditivo_listar'), 'termo_aditivo_listar'
