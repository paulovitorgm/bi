from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from apps.pessoas.forms import BuscarPessoaForm, PessoaForm
from apps.pessoas.models import PessoaModel


class PessoaCreate(CreateView):
    model = PessoaModel
    template_name = 'pessoas/cadastrar.html'
    form_class = PessoaForm
    success_url = reverse_lazy('listar-pessoas')


class PessoaUpdate(UpdateView):
    model = PessoaModel
    template_name = 'pessoas/form.html'
    form_class = PessoaForm
    context_object_name = 'editar-pessoa'
    slug_field = 'matricula'
    slug_url_kwarg = 'matricula'
    success_url = reverse_lazy('listar-pessoas')


class PessoaDetail(DetailView):
    model = PessoaModel
    template_name = 'pessoas/detalhar.html'
    context_object_name = 'pessoa'
    slug_field = 'matricula'
    slug_url_kwarg = 'matricula'


class PessoaListView(ListView):
    model = PessoaModel
    template_name = 'pessoas/listar.html'
    context_object_name = 'pessoas'
    paginate_by = 20


class PessoaDelete(DeleteView):
    model = PessoaModel
    template_name = 'pessoas/confirmacao.html'
    context_object_name = 'pessoa'
    slug_field = 'matricula'
    slug_url_kwarg = 'matricula'
    success_url = reverse_lazy('listar-pessoas')


def buscar_pessoa_para_excluir(request):
    if request.method == 'POST':
        form = BuscarPessoaForm(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data.get('matricula')
            try:
                matr = PessoaModel.objects.get(matricula=matricula)
                return redirect(
                    'confirmar-exclusao-pessoa',
                    matricula=matr.matricula,
                )
            except PessoaModel.DoesNotExist:
                form.add_error(field='matricula', error='Matrícula não encontrada')
            except PessoaModel.MultipleObjectsReturned:
                form.add_error(
                    field='matricula',
                    error='Existe mais de um pessoa com a mesma matrícula',
                )
    else:
        form = BuscarPessoaForm()
    return render(request, 'pessoas/busca.html', {'form': form})


# Modais


class ModalCreateView(CreateView):
    label_field = None

    def get_label(self, obj):
        if self.label_field:
            return getattr(obj, self.label_field)
        return str(obj)

    def form_valid(self, form):
        obj = form.save()

        return JsonResponse({
            'success': True,
            'id': obj.pk,
            'text': self.get_label(obj),
        })


class ModalMixin:
    """
    Funcionalidades comuns para todas as views carregadas em modal.
    """

    label_field = None

    def get_label(self, obj):
        if self.label_field:
            return getattr(obj, self.label_field)
        return str(obj)

    def json_success(self, obj, message='Operação realizada com sucesso.'):
        return JsonResponse({
            'success': True,
            'id': obj.pk,
            'text': self.get_label(obj),
            'message': message,
        })

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form),
            status=400,
        )
