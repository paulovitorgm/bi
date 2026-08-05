from django.http import JsonResponse
from django.views.generic import CreateView

from apps.processos.forms.cadastrosform import (
    AbrangenciaForm,
    ParticipeForm,
    TipoInstrumentoForm,
)
from apps.processos.forms.entidadeparceiraform import EntidadeParceiraForm
from apps.processos.forms.modalidadeform import ModalidadeForm
from apps.processos.forms.naturezaform import NaturezaForm
from apps.processos.forms.unidadeform import UnidadeForm
from apps.processos.models.abrangencia import Abrangencia
from apps.processos.models.entidadeparceira import EntidadeParceira
from apps.processos.models.modalidade import Modalidade
from apps.processos.models.natureza import Natureza
from apps.processos.models.participesmodel import ParticipesModel
from apps.processos.models.tipoinstrumento import TipoInstrumento
from apps.processos.models.unidade import Unidade
from apps.pessoas.forms import PessoaForm
from apps.pessoas.models import PessoaModel


class ModalCadastroCreateView(CreateView):
    template_name = 'processos/modais/form.html'
    titulo = 'Novo cadastro'

    def form_valid(self, form):
        objeto = form.save()
        return JsonResponse({'id': objeto.pk, 'text': str(objeto)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        return context


class UnidadeModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = Unidade, UnidadeForm, 'Nova unidade'


class ParticipeModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = ParticipesModel, ParticipeForm, 'Novo partícipe'


class ModalidadeModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = Modalidade, ModalidadeForm, 'Nova modalidade'


class NaturezaModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = Natureza, NaturezaForm, 'Nova natureza'


class AbrangenciaModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = Abrangencia, AbrangenciaForm, 'Nova abrangência'


class EntidadeModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = EntidadeParceira, EntidadeParceiraForm, 'Nova entidade parceira'


class TipoInstrumentoModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = TipoInstrumento, TipoInstrumentoForm, 'Novo tipo de instrumento'


class PessoaModalCreateView(ModalCadastroCreateView):
    model, form_class, titulo = PessoaModel, PessoaForm, 'Nova pessoa'
