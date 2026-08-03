from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from apps.processos.forms import ModalidadeForm
from apps.processos.models import Modalidade


class ModalidadeListView(ListView):
    model = Modalidade
    template_name = 'processos/modalidade/listar.html'
    context_object_name = 'modalidades'


class ModalidadeCreateView(CreateView):
    model = Modalidade
    form_class = ModalidadeForm
    template_name = 'processos/modalidade/form.html'
    success_url = reverse_lazy('modalidade_listar')


class ModalidadeUpdateView(UpdateView):
    model = Modalidade
    form_class = ModalidadeForm
    template_name = 'processos/modalidade/form.html'
    success_url = reverse_lazy('modalidade_listar')


class ModalidadeDeleteView(DeleteView):
    model = Modalidade
    template_name = 'processos/modalidade/deletar.html'
    success_url = reverse_lazy('modalidade_listar')
