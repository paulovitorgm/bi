from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.controle_de_processos_capro.forms import (
    ControleDeProcessosForm,
    CoordenadorForm,
)
from apps.controle_de_processos_capro.models import ControleDeProcessosModel, CoordenadorModel


class ControleDeProcessosCreate(CreateView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/cadastrar_processo.html'
    form_class = ControleDeProcessosForm
    success_url = reverse_lazy('controle_de_processos_capro:listar')

class ControleDeProcessosListView(ListView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/lista_processos.html'
    context_object_name = 'lista'

class ControleDeProcessosUpdate(UpdateView):
    pass

class ControleDeProcessosDelete(DeleteView):
    pass

class ControleDeProcessosDetail(DetailView):
    pass



class CoordenadorCreate(CreateView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/cadastrar_coordenador.html'
    form_class = CoordenadorForm
    success_url = reverse_lazy('listar-coordenadores')


class CoordenadorListView(ListView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/lista_coordenadores.html'
    context_object_name = 'coordenadores'
