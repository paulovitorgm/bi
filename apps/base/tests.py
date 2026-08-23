from django.db import OperationalError
from django.test import RequestFactory, SimpleTestCase

from base_de_dados_bi.error_views import page_not_found
from base_de_dados_bi.middleware import DatabaseUnavailableMiddleware


class ErrorPageTests(SimpleTestCase):
    def setUp(self):
        self.request = RequestFactory().get('/inexistente/')

    def test_404_uses_custom_error_page(self):
        response = page_not_found(self.request)

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'P', status_code=404)

    def test_database_unavailable_returns_503(self):
        middleware = DatabaseUnavailableMiddleware(lambda request: None)

        response = middleware.process_exception(self.request, OperationalError())

        self.assertEqual(response.status_code, 503)
