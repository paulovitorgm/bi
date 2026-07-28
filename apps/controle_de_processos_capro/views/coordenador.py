from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.controle_de_processos_capro.forms import CoordenadorForm
from apps.controle_de_processos_capro.models.coordenador import CoordenadorModel


class CoordenadorCreate(CreateView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/coordenadores/cadastrar.html'
    form_class = CoordenadorForm
    success_url = reverse_lazy('listar-coordenadores')


class CoordenadorListView(ListView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/coordenadores/listar.html'
    context_object_name = 'coordenadores'


class CoordenadorUpdate(UpdateView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/coordenadores/editar.html'
    form_class = CoordenadorForm

    def get_success_url(self):
        return reverse(
            'editar-coordenador',
            kwargs={'id': self.object.pk},
        )


class CoordenadorDelete(DeleteView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/deletar_coordenador.html'


class CoordenadorDetail(DetailView):
    model = CoordenadorModel
    template_name = 'controle_de_processos/detail.html'
    context_object_name = 'coordenador'
