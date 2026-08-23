from rest_framework.routers import DefaultRouter

from apps.processos.api import (
    AbrangenciaViewSet,
    EntidadeParceiraViewSet,
    ModalidadeViewSet,
    NaturezaViewSet,
    ParticipesViewSet,
    PessoaViewSet,
    ProcessoProjetoViewSet,
    TermoAditivoViewSet,
    TipoInstrumentoViewSet,
    UnidadeViewSet,
)

router = DefaultRouter()
router.register('processos', ProcessoProjetoViewSet, basename='api-processo')
router.register('termos-aditivos', TermoAditivoViewSet, basename='api-termo-aditivo')
router.register('pessoas', PessoaViewSet, basename='api-pessoa')
router.register('abrangencias', AbrangenciaViewSet, basename='api-abrangencia')
router.register('entidades-parceiras', EntidadeParceiraViewSet, basename='api-entidade')
router.register('modalidades', ModalidadeViewSet, basename='api-modalidade')
router.register('naturezas', NaturezaViewSet, basename='api-natureza')
router.register('participes', ParticipesViewSet, basename='api-participe')
router.register(
    'tipos-instrumento', TipoInstrumentoViewSet, basename='api-tipo-instrumento'
)
router.register('unidades', UnidadeViewSet, basename='api-unidade')

urlpatterns = router.urls
