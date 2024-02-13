from django.test import TestCase

from api.views import DashboardViewSet
from rest_framework.test import APIRequestFactory

class DashboardViewSetTestCase(TestCase):
    def test_dashboard_view(self):
        factory = APIRequestFactory()

        request = factory.get('/dashboard/')

        view = DashboardViewSet.as_view()
        response = view(request)

        # Verifica se a resposta retornou um código de status HTTP 200
        self.assertEqual(response.status_code, 200)

        self.assertIn('vendas', response.data)
