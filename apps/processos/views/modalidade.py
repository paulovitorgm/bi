from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from apps.base.mixins import AuditoriaUsuarioMixin, PaginacaoMixin
from apps.processos.forms.modalidadeform import ModalidadeForm
from apps.processos.models.modalidade import Modalidade


class ModalidadeListView(PaginacaoMixin, ListView):
    model = Modalidade
    template_name = 'processos/modalidade/listar.html'
    context_object_name = 'modalidades'
    paginate_by = 20


class ModalidadeCreateView(AuditoriaUsuarioMixin, CreateView):
    model = Modalidade
    form_class = ModalidadeForm
    template_name = 'processos/modalidade/form.html'
    success_url = reverse_lazy('modalidade_listar')


class ModalidadeUpdateView(AuditoriaUsuarioMixin, UpdateView):
    model = Modalidade
    form_class = ModalidadeForm
    template_name = 'processos/modalidade/form.html'
    success_url = reverse_lazy('modalidade_listar')


class ModalidadeDeleteView(DeleteView):
    model = Modalidade
    template_name = 'processos/modalidade/deletar.html'
    success_url = reverse_lazy('modalidade_listar')
