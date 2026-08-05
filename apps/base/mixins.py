class AuditoriaUsuarioMixin:
    """Registra o usuário autenticado responsável pela inclusão ou alteração."""

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if not form.instance.pk:
                form.instance.criado_por = self.request.user
            form.instance.atualizado_por = self.request.user
        return super().form_valid(form)


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
