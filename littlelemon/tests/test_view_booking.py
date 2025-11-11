from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import BookingTable
from restaurant.serializers import BookingSerializer
from django.contrib.auth.models import User
from datetime import date


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.menu_item1 = BookingTable.objects.create(name="Buhari", noOfGuests=10, bookingDate="2025-12-11")
        self.menu_item2 = BookingTable.objects.create(name="Sangeetha", noOfGuests=15, bookingDate="2025-12-11")

    def test_getall(self):
        response = self.client.get('/api/booking/items/')
        menu_items = BookingTable.objects.all()
        serializer = BookingSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)