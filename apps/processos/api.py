from rest_framework import serializers, viewsets

from apps.pessoas.models import PessoaModel
from apps.processos.models import (
    Abrangencia,
    EntidadeParceira,
    Modalidade,
    Natureza,
    ParticipesModel,
    ProcessoProjeto,
    TipoInstrumento,
    Unidade,
)
from apps.processos.models.termosadtivos import TermosAdtivos


class TermoAditivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermosAdtivos
        fields = ['id', 'processo', 'termo', 'dt_assinatura', 'dt_termino', 'valor']


class ProcessoProjetoSerializer(serializers.ModelSerializer):
    termos_aditivos = TermoAditivoSerializer(many=True, read_only=True)

    class Meta:
        model = ProcessoProjeto
        fields = [
            'id',
            'processo',
            'numero_convenio',
            'nome_do_processo',
            'ementa',
            'participes',
            'unidade_interessada',
            'tipo_instrumento',
            'modalidade',
            'esfera_administrativa',
            'natureza',
            'abrangencia',
            'entidade_parceira',
            'coordenador',
            'supervisor_academico',
            'relator',
            'substituto',
            'valor_inicial',
            'valor_total',
            'custos_indiretos',
            'dt_inicio',
            'dt_termino',
            'dt_assinatura',
            'ods_onu',
            'termos_aditivos',
            'criado_em',
            'atualizado_em',
        ]
        read_only_fields = ['id', 'valor_total', 'criado_em', 'atualizado_em']

    def validate(self, attrs):
        inicio = attrs.get('dt_inicio', getattr(self.instance, 'dt_inicio', None))
        termino = attrs.get('dt_termino', getattr(self.instance, 'dt_termino', None))
        if inicio and termino and termino < inicio:
            raise serializers.ValidationError({
                'dt_termino': 'A data de término não pode ser anterior à data de início.'
            })
        return attrs


class AuditoriaAPIViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user, atualizado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(atualizado_por=self.request.user)


class ProcessoProjetoViewSet(AuditoriaAPIViewSet):
    queryset = ProcessoProjeto.objects.all().prefetch_related('termos_aditivos')
    serializer_class = ProcessoProjetoSerializer
    lookup_field = 'processo'
    search_fields = ['processo', 'numero_convenio', 'nome_do_processo']
    ordering_fields = ['processo', 'dt_inicio', 'dt_termino', 'valor_total']

    def perform_create(self, serializer):
        processo = serializer.save(
            criado_por=self.request.user, atualizado_por=self.request.user
        )
        processo.recalcular_valor_total()

    def perform_update(self, serializer):
        processo = serializer.save(atualizado_por=self.request.user)
        processo.recalcular_valor_total()


class TermoAditivoViewSet(AuditoriaAPIViewSet):
    queryset = TermosAdtivos.objects.select_related('processo')
    serializer_class = TermoAditivoSerializer
    search_fields = ['termo', 'processo__processo']
    ordering_fields = ['termo', 'dt_assinatura', 'dt_termino', 'valor']


def readonly_viewset(model):
    class DomainViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = model.objects.all()

    serializer_meta = type('Meta', (), {'model': model, 'fields': '__all__'})
    DomainViewSet.serializer_class = type(
        f'{model.__name__}Serializer',
        (serializers.ModelSerializer,),
        {'Meta': serializer_meta},
    )

    return DomainViewSet


PessoaViewSet = readonly_viewset(PessoaModel)
AbrangenciaViewSet = readonly_viewset(Abrangencia)
EntidadeParceiraViewSet = readonly_viewset(EntidadeParceira)
ModalidadeViewSet = readonly_viewset(Modalidade)
NaturezaViewSet = readonly_viewset(Natureza)
ParticipesViewSet = readonly_viewset(ParticipesModel)
TipoInstrumentoViewSet = readonly_viewset(TipoInstrumento)
UnidadeViewSet = readonly_viewset(Unidade)
