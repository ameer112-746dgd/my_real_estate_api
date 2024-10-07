from django.db import models

# Create your models here.
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='properties/')
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    noRooms = models.IntegerField()
    noBath = models.IntegerField()
    size = models.FloatField()  # Size in square meters

    def __str__(self):
        return self.name
