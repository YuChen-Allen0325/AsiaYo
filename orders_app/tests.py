from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from orders_app.views import OrdersValidationView

class OrdersTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = OrdersValidationView.as_view()
        self.url = reverse('orders')

    def test_orders_post(self):

        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "1050",
            "currency": "TWD"
        }

        request = self.factory.post(self.url, data, format='json')
        response = self.view(request)
        print("\n",response.data,"\n")
        self.assertEqual(response.status_code, 200)