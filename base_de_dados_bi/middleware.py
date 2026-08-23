import logging

from django.conf import settings
from django.db import InterfaceError, OperationalError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse

logger = logging.getLogger(__name__)


class DatabaseUnavailableMiddleware:
    """Returns a safe response when PostgreSQL is unavailable."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):  # ruff: ignore[no-self-use]
        if not isinstance(exception, (OperationalError, InterfaceError)):
            return None
        logger.exception('Database unavailable during %s', request.path)
        return render(request, '_errors/503.html', status=503)


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

        # A API usa a autenticação do Django REST Framework e deve retornar JSON,
        # nunca um redirecionamento para a tela HTML de login.
        if path.startswith('/api/'):
            return self.get_response(request)

        if path in settings.PUBLIC_URLS:
            return self.get_response(request)

        if path.startswith(settings.STATIC_URL):
            return self.get_response(request)

        if settings.MEDIA_URL and path.startswith(settings.MEDIA_URL):
            return self.get_response(request)
        return redirect(f'{reverse("login")}?next={request.get_full_path()}')


class ApiCorsMiddleware:
    """Permite origens explicitamente liberadas acessarem a API no navegador."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        origin = request.headers.get('Origin')
        allowed = origin and origin in settings.CORS_ALLOWED_ORIGINS
        if request.path.startswith('/api/') and request.method == 'OPTIONS':
            response = HttpResponse(status=204)
        else:
            response = self.get_response(request)
        if allowed:
            response['Access-Control-Allow-Origin'] = origin
            response['Vary'] = 'Origin'
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
        return response
