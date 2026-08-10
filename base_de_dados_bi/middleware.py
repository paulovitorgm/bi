import logging

from django.conf import settings
from django.db import InterfaceError, OperationalError
from django.shortcuts import redirect, render
from django.urls import reverse

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

        if path in settings.PUBLIC_URLS:
            return self.get_response(request)

        if path.startswith(settings.STATIC_URL):
            return self.get_response(request)

        if settings.MEDIA_URL and path.startswith(settings.MEDIA_URL):
            return self.get_response(request)
        return redirect(f'{reverse("login")}?next={request.get_full_path()}')
