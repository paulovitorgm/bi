from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.base.mixins import AuditoriaUsuarioMixin, PaginacaoMixin
from apps.pessoas.models import PessoaModel
from apps.processos.forms.itemplanodespesaform import ItemPlanoDespesaForm
from apps.processos.forms.pessoaform import PessoaForm
from apps.processos.forms.processoprojetoform import (
    ProcessoProjetoForm,
    TermoAditivoFormSet,
)
from apps.processos.forms.tipodespesaform import TipoDespesaForm
from apps.processos.models.itemplanodespesa import ItemPlanoDespesa
from apps.processos.models.processoprojeto import ProcessoProjeto
from apps.processos.models.tipodespesa import TipoDespesa


class ProcessoListView(PaginacaoMixin, ListView):
    model = ProcessoProjeto
    template_name = 'processos/processos/listar.html'
    context_object_name = 'processos'
    paginate_by = 20
    ordering = ['-id']

    def get_queryset(self):
        queryset = ProcessoProjeto.objects.select_related(
            'coordenador',
            'entidade_parceira',
            'relator',
            'substituto',
        ).prefetch_related('modalidade', 'natureza', 'unidade_interessada')
        busca = self.request.GET.get('q', '').strip()
        if busca:
            config = 'portuguese'
            vector = (
                SearchVector('processo', weight='A', config=config)
                + SearchVector('numero_convenio', weight='A', config=config)
                + SearchVector('nome_do_processo', weight='B', config=config)
                + SearchVector('coordenador__nome', weight='C', config=config)
            )
            query = SearchQuery(busca, config=config, search_type='websearch')
            queryset = queryset.annotate(
                rank=SearchRank(vector, query)
                .filter(rank__gte=0.1)
                .order_by('-rank', '-dt_assinatura')
            )
        else:
            queryset = queryset.order_by('-dt_assinatura')
        return queryset


class TermoAditivoFormsetMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['termo_formset'] = TermoAditivoFormSet(
            self.request.POST or None,
            instance=self.object,
        )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        termo_formset = context['termo_formset']
        if not termo_formset.is_valid():
            return self.render_to_response(context)
        response = super().form_valid(form)
        termo_formset.instance = self.object
        termo_formset.save()
        return response


class ProcessoCreateView(AuditoriaUsuarioMixin, TermoAditivoFormsetMixin, CreateView):
    model = ProcessoProjeto
    form_class = ProcessoProjetoForm
    template_name = 'processos/processos/form.html'
    success_url = reverse_lazy('processo_listar')


class ProcessoUpdateView(AuditoriaUsuarioMixin, TermoAditivoFormsetMixin, UpdateView):
    model = ProcessoProjeto
    form_class = ProcessoProjetoForm
    template_name = 'processos/processos/form.html'
    success_url = reverse_lazy('processo_listar')

    slug_field = 'processo'
    slug_url_kwarg = 'processo'


class ProcessoDeleteView(DeleteView):
    model = ProcessoProjeto
    template_name = 'processos/processos/deletar.html'
    success_url = reverse_lazy('processo_listar')

    slug_field = 'processo'
    slug_url_kwarg = 'processo'


class ProcessoDetailView(DetailView):
    model = ProcessoProjeto
    template_name = 'processos/processos/detalhes.html'
    context_object_name = 'processo'
    slug_field = 'processo'
    slug_url_kwarg = 'processo'


# ==========================================
# 2. VIEWS DO PLANO DE APLICAÇÃO DAS DESPESAS
# ==========================================


class ItemPlanoDespesaCreateView(AuditoriaUsuarioMixin, CreateView):
    model = ItemPlanoDespesa
    form_class = ItemPlanoDespesaForm  # Usando o Form do Bootstrap
    template_name = 'projetos/item_despesa_form.html'

    def form_valid(self, form):
        form.instance.processo_id = self.kwargs['processo_pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('processo_detail', kwargs={'pk': self.kwargs['processo_pk']})


class ItemPlanoDespesaUpdateView(AuditoriaUsuarioMixin, UpdateView):
    model = ItemPlanoDespesa
    form_class = ItemPlanoDespesaForm  # Usando o Form do Bootstrap
    template_name = 'projetos/item_despesa_form.html'

    def get_success_url(self):
        return reverse('processo_detail', kwargs={'pk': self.object.processo.pk})


class ItemPlanoDespesaDeleteView(DeleteView):
    model = ItemPlanoDespesa
    template_name = 'projetos/item_despesa_confirm_delete.html'

    def get_success_url(self):
        return reverse('processo_detail', kwargs={'pk': self.object.processo.pk})


# ==========================================
# 3. VIEWS DE TABELAS DE DOMÍNIO / DIMENSÕES
# ==========================================


class PessoaListView(ListView):
    model = PessoaModel
    template_name = 'dominios/pessoa_list.html'
    context_object_name = 'pessoas'
    paginate_by = 20


class PessoaCreateView(CreateView):
    model = PessoaModel
    form_class = PessoaForm
    template_name = 'dominios/form.html'
    success_url = reverse_lazy('pessoa_list')


class TipoDespesaListView(ListView):
    model = TipoDespesa
    template_name = 'dominios/tipo_despesa_list.html'
    context_object_name = 'tipos_despesa'


class TipoDespesaCreateView(CreateView):
    model = TipoDespesa
    form_class = TipoDespesaForm
    template_name = 'dominios/tipo_despesa_form.html'
    success_url = reverse_lazy('tipo_despesa_list')
