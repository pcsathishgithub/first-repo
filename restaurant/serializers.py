from rest_framework import serializers
from .models import MenuTable, BookingTable

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = ['id', 'title', 'price', 'inventory']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = ['id', 'name', 'noOfGuests', 'bookingDate']
        