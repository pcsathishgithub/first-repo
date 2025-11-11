from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuTable
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User



class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.menu_item1 = MenuTable.objects.create(title="Burger", price=10.99, inventory=50)
        self.menu_item2 = MenuTable.objects.create(title="Pizza", price=12.99, inventory=40)

    def test_getall(self):
        response = self.client.get('/api/menu/items/')
        menu_items = MenuTable.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)