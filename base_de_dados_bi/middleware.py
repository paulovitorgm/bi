from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    """
    Exige autenticação para todas as páginas da aplicação,
    exceto as URLs configuradas em settings.PUBLIC_URLS e os
    arquivos estáticos e de mídia.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if request.user.is_authenticated:
            return self.get_response(request)

        if path in settings.PUBLIC_URLS:
            return self.get_response(request)

        if path.startswith(settings.STATIC_URL):
            return self.get_response(request)

        if settings.MEDIA_URL and path.startswith(settings.MEDIA_URL):
            return self.get_response(request)
        return redirect(
            f"{reverse('login')}?next={request.get_full_path()}"
        )