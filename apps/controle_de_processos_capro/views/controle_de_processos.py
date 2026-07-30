from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.controle_de_processos_capro.forms import (
    BuscarProcessoForm,
    ControleDeProcessosForm,
)
from apps.controle_de_processos_capro.models.controle_de_processos import (
    ControleDeProcessosModel,
)


class ControleDeProcessosCreate(CreateView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/processos/cadastrar.html'
    form_class = ControleDeProcessosForm
    success_url = reverse_lazy('listar-processos')


class ControleDeProcessosListView(ListView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/processos/listar.html'
    context_object_name = 'processos'


class ControleDeProcessosUpdate(UpdateView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/processos/form.html'
    form_class = ControleDeProcessosForm
    context_object_name = 'processo'
    slug_field = 'processo_sei'
    slug_url_kwarg = 'processo_sei'

    def get_success_url(self):
        return reverse(
            'detalhar-processo',
            kwargs={'processo_sei': self.object.processo_sei},
        )


class ControleDeProcessosDelete(DeleteView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/processos/confirmacao.html'
    success_url = reverse_lazy('listar-processos')
    slug_field = 'processo_sei'
    slug_url_kwarg = 'processo_sei'


class ControleDeProcessosDetail(DetailView):
    model = ControleDeProcessosModel
    template_name = 'controle_de_processos/processos/detalhar.html'
    context_object_name = 'processo'
    slug_field = 'processo_sei'
    slug_url_kwarg = 'processo_sei'


def buscar_processo_para_excluir(request):

    if request.method == 'POST':
        form = BuscarProcessoForm(request.POST)

        if form.is_valid():
            processo_sei = form.cleaned_data.get('processo_sei')

            try:
                processo = ControleDeProcessosModel.objects.get(processo_sei=processo_sei)

                return redirect(
                    'confirmar-exclusao-processo',
                    processo_sei=processo.processo_sei,
                )

            except ControleDeProcessosModel.DoesNotExist:
                form.add_error('processo_sei', 'Não existe um processo com esse número.')

            except ControleDeProcessosModel.MultipleObjectsReturned:
                form.add_error(
                    'processo_sei', 'Existe mais de um processo com esse número.'
                )

    else:
        form = BuscarProcessoForm()

    return render(
        request,
        'controle_de_processos/processos/busca.html',
        {
            'form': form,
        },
    )
