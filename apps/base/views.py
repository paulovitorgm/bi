from django.shortcuts import render

from apps.pessoas.models import PessoaModel
from apps.processos.models.processoprojeto import ProcessoProjeto


def index(request):
    return render(request, 'index.html', {
        'total_processos': ProcessoProjeto.objects.count(),
        'total_pessoas': PessoaModel.objects.count(),
    })
