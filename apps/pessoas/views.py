from django.db.models import Q
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from apps.base.mixins import AuditoriaUsuarioMixin, PaginacaoMixin
from apps.pessoas.forms import PessoaForm, UnidadeDeLotacaoForm
from apps.pessoas.models import PessoaModel, UnidadeDeLotacao


class PessoaCreate(AuditoriaUsuarioMixin, CreateView):
    model = PessoaModel
    template_name = 'pessoas/form.html'
    form_class = PessoaForm
    success_url = reverse_lazy('listar-pessoas')


class PessoaUpdate(AuditoriaUsuarioMixin, UpdateView):
    model = PessoaModel
    template_name = 'pessoas/form.html'
    form_class = PessoaForm
    context_object_name = 'editar-pessoa'
    slug_field = 'matricula'
    slug_url_kwarg = 'matricula'
    success_url = reverse_lazy('listar-pessoas')


class PessoaListView(PaginacaoMixin, ListView):
    model = PessoaModel
    template_name = 'pessoas/listar.html'
    context_object_name = 'pessoas'
    paginate_by = 20

    def get_queryset(self):
        queryset = PessoaModel.objects.all()
        busca = self.request.GET.get('q', '').strip()
        if busca:
            queryset = queryset.filter(
                Q(nome__icontains=busca) | Q(matricula__icontains=busca)
            )
        return queryset


class PessoaDelete(DeleteView):
    model = PessoaModel
    template_name = 'pessoas/confirmacao.html'
    context_object_name = 'pessoa'
    slug_field = 'matricula'
    slug_url_kwarg = 'matricula'
    success_url = reverse_lazy('listar-pessoas')


class UnidadeDeLotacaoModalCreateView(CreateView):
    """Cria uma unidade e a devolve ao seletor da pessoa via modal."""

    model = UnidadeDeLotacao
    form_class = UnidadeDeLotacaoForm
    template_name = 'processos/modais/form.html'
    titulo = 'Nova unidade de lotação'

    def form_valid(self, form):  # ruff: ignore[no-self-use]
        unidade = form.save()
        return JsonResponse({'id': unidade.pk, 'text': str(unidade)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context
