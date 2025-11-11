from django.test import TestCase
from restaurant.models import MenuTable

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title="IceCream", price=80)
        self.assertEqual(str(item), "IceCream : 80")
        