class AuditoriaUsuarioMixin:
    """Registra o usuário autenticado responsável pela inclusão ou alteração."""

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if not form.instance.pk:
                form.instance.criado_por = self.request.user
            form.instance.atualizado_por = self.request.user
        return super().form_valid(form)
