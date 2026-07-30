from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.processos.forms import (
    ItemPlanoDespesaForm,
    PessoaForm,
    ProcessoProjetoForm,
    TipoDespesaForm,
)
from apps.processos.models import (
    ItemPlanoDespesa,
    PessoaModel,
    ProcessoProjeto,
    TipoDespesa,
)

# ==========================================
# 1. VIEWS DE PROCESSO / PROJETO
# ==========================================


class ProcessoListView(ListView):
    model = ProcessoProjeto
    template_name = 'processos/listar.html'
    context_object_name = 'processos'
    paginate_by = 15

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .select_related(
                'unidade_interessada',
                'modalidade',
                'coordenador',
                'entidade_parceira',
            )
        )

        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(numero_processo_limpo__icontains=q)
                | Q(coordenador__nome__icontains=q)
                | Q(numero_convenio__icontains=q)
            )
        return queryset


class ProcessoDetailView(DetailView):
    model = ProcessoProjeto
    template_name = 'processos/detalhar.html'
    context_object_name = 'processo'

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related(
                'unidade_interessada',
                'modalidade',
                'natureza',
                'abrangencia',
                'entidade_parceira',
                'coordenador',
                'supervisor_academico',
                'relator',
                'substituto',
            )
            .prefetch_related('despesas__tipo_despesa')
        )


class ProcessoCreateView(CreateView):
    model = ProcessoProjeto
    form_class = ProcessoProjetoForm
    template_name = 'processos/processo_form.html'
    success_url = reverse_lazy('processo_list')


class ProcessoUpdateView(UpdateView):
    model = ProcessoProjeto
    form_class = ProcessoProjetoForm
    template_name = 'processos/processo_form.html'

    def get_success_url(self):
        return reverse('processo_detail', kwargs={'pk': self.object.pk})


class ProcessoDeleteView(DeleteView):
    model = ProcessoProjeto
    template_name = 'processos/confirmacao.html'
    success_url = reverse_lazy('processo_list')


# ==========================================
# 2. VIEWS DO PLANO DE APLICAÇÃO DAS DESPESAS
# ==========================================


class ItemPlanoDespesaCreateView(CreateView):
    model = ItemPlanoDespesa
    form_class = ItemPlanoDespesaForm  # Usando o Form do Bootstrap
    template_name = 'projetos/item_despesa_form.html'

    def form_valid(self, form):
        form.instance.processo_id = self.kwargs['processo_pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('processo_detail', kwargs={'pk': self.kwargs['processo_pk']})


class ItemPlanoDespesaUpdateView(UpdateView):
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
    template_name = 'dominios/pessoa_form.html'
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
