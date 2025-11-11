from django.db import models

# Create your models here.
class BookingTable(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=255, null=True)
    noOfGuests = models.PositiveIntegerField(default=0)
    bookingDate = models.DateField(null=True)

class MenuTable(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    inventory = models.PositiveIntegerField(default=0)
    #add the following method in Menu class
    #add the following method in Menu class
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
