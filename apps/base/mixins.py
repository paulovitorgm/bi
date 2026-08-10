import logging

from django.contrib import messages
from django.db import IntegrityError
from django.db.models.deletion import ProtectedError, RestrictedError

logger = logging.getLogger(__name__)


class AuditoriaUsuarioMixin:
    """Registra o usuário autenticado responsável pela inclusão ou alteração."""

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if not form.instance.pk:
                form.instance.criado_por = self.request.user
            form.instance.atualizado_por = self.request.user
        return super().form_valid(form)


class TrataErroIntegridadeMixin:
    """Avoids a 500 response when concurrent writes violate a constraint."""

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            logger.exception('Integrity conflict while saving %s', self.model.__name__)
            form.add_error(
                None,
                'Nao foi possivel salvar porque ja existe um registro com esses dados.',
            )
            return self.form_invalid(form)


class TrataExclusaoProtegidaMixin:
    """Explains when relationships prevent an object from being deleted."""

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except (ProtectedError, RestrictedError):
            logger.info('Deletion blocked for %s', self.model.__name__)
            messages.error(
                self.request,
                'Este registro nao pode ser excluido porque esta vinculado a outros dados.',
            )
            return self.render_to_response(self.get_context_data())


class PaginacaoMixin:
    """Paginação consistente, com tamanho de página controlado pela interface."""

    paginate_by = 20
    page_sizes = (20, 50, 100)

    def get_paginate_by(self, queryset):
        try:
            per_page = int(self.request.GET.get('per_page', self.paginate_by))
        except (TypeError, ValueError):
            per_page = self.paginate_by
        return per_page if per_page in self.page_sizes else self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querydict = self.request.GET.copy()
        querydict.pop('page', None)
        context['querystring'] = querydict.urlencode()
        context['page_sizes'] = self.page_sizes
        context['selected_per_page'] = self.get_paginate_by(None)
        return context
