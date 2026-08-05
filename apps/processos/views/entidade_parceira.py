from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from apps.base.mixins import AuditoriaUsuarioMixin, PaginacaoMixin
from apps.processos.forms.entidadeparceiraform import EntidadeParceiraForm
from apps.processos.models.entidadeparceira import EntidadeParceira


class EntidadeParceiraListView(PaginacaoMixin, ListView):
    model = EntidadeParceira
    template_name = 'processos/entidade_parceira/listar.html'
    context_object_name = 'entidades'
    paginate_by = 20


class EntidadeParceiraCreateView(AuditoriaUsuarioMixin, CreateView):
    model = EntidadeParceira
    form_class = EntidadeParceiraForm
    template_name = 'processos/entidade_parceira/form.html'
    success_url = reverse_lazy('entidade_parceira_listar')


class EntidadeParceiraUpdateView(AuditoriaUsuarioMixin, UpdateView):
    model = EntidadeParceira
    form_class = EntidadeParceiraForm
    template_name = 'processos/entidade_parceira/form.html'
    success_url = reverse_lazy('entidade_parceira_listar')


class EntidadeParceiraDeleteView(DeleteView):
    model = EntidadeParceira
    template_name = 'processos/entidade_parceira/deletar.html'
    success_url = reverse_lazy('entidade_parceira_listar')
