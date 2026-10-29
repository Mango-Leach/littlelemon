from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import MenuItem

class MenuAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = MenuItem.objects.create(title="Bruschetta", price="8.50", inventory=12)

    def test_menu_list_returns_200(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)

    def test_menu_item_is_in_response(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Bruschetta")

# TODO: Add tests for create/update/delete menu actions, booking authentication,
# booking CRUD, registration validation, and token issuance.
