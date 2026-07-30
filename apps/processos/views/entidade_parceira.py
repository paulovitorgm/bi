from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from apps.processos.forms import EntidadeParceiraForm
from apps.processos.models import EntidadeParceira


class EntidadeParceiraListView(ListView):
    model = EntidadeParceira
    template_name = 'processos/entidade_parceira/listar.html'
    context_object_name = 'entidades'


class EntidadeParceiraCreateView(CreateView):
    model = EntidadeParceira
    form_class = EntidadeParceiraForm
    template_name = 'processos/entidade_parceira/form.html'
    success_url = reverse_lazy('entidade_parceira_list')


class EntidadeParceiraUpdateView(UpdateView):
    model = EntidadeParceira
    form_class = EntidadeParceiraForm
    template_name = 'processos/entidade_parceira/form.html'
    success_url = reverse_lazy('entidade_parceira_list')


class EntidadeParceiraDeleteView(DeleteView):
    model = EntidadeParceira
    template_name = 'processos/entidade_parceira/deletar.html'
    success_url = reverse_lazy('entidade_parceira_list')
