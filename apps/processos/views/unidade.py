from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.processos.forms import UnidadeForm
from apps.processos.models.unidade import Unidade


class UnidadeListView(ListView):
    model = Unidade
    template_name = 'processos/unidade/listar.html'
    context_object_name = 'unidades'


class UnidadeCreateView(CreateView):
    model = Unidade
    form_class = UnidadeForm
    template_name = 'processos/unidade/form.html'
    success_url = reverse_lazy('unidade_listar')


class UnidadeUpdateView(UpdateView):
    model = Unidade
    form_class = UnidadeForm
    template_name = 'processos/unidade/form.html'
    success_url = reverse_lazy('unidade_listar')


class UnidadeDeleteView(DeleteView):
    model = Unidade
    template_name = 'processos/unidade/deletar.html'
    success_url = reverse_lazy('unidade_listar')
