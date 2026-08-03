from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from apps.processos.forms import NaturezaForm
from apps.processos.models import Natureza


class NaturezaListView(ListView):
    model = Natureza
    template_name = 'processos/natureza/listar.html'
    context_object_name = 'naturezas'


class NaturezaCreateView(CreateView):
    model = Natureza
    form_class = NaturezaForm
    template_name = 'processos/natureza/form.html'
    success_url = reverse_lazy('natureza_listar')


class NaturezaUpdateView(UpdateView):
    model = Natureza
    form_class = NaturezaForm
    template_name = 'processos/natureza/form.html'
    success_url = reverse_lazy('natureza_listar')


class NaturezaDeleteView(DeleteView):
    model = Natureza
    template_name = 'processos/natureza/deletar.html'
    success_url = reverse_lazy('natureza_listar')
