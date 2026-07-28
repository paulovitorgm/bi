from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.controle_de_processos_capro.forms import ControleDeProcessosForm
from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
)


class ControleDeProcessosCreate(CreateView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/cadastrar.html'
    form_class = ControleDeProcessosForm
    success_url = reverse_lazy('listar-processos')


class ControleDeProcessosListView(ListView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/listar.html'
    context_object_name = 'lista'


class ControleDeProcessosUpdate(UpdateView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/atualizar_processo.html'
    form_class = ControleDeProcessosForm
    success_url = reverse_lazy('listar-processos')


class ControleDeProcessosDelete(DeleteView):
    pass


class ControleDeProcessosDetail(DetailView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/detail.html'
    context_object_name = 'processo'
