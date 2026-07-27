from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.controle_de_processos_capro.forms import ControleDeProcessosForm
from apps.controle_de_processos_capro.models import ControleDeProcessosModel


class ControleDeProcessosListView(ListView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/lista.html'
    context_object_name = 'processos'


class ControleDeProcessosCreate(CreateView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/cadastrar_coordenador.html'
    form_class = ControleDeProcessosForm
    success_url = reverse_lazy('controle_de_processos_capro:listar')
