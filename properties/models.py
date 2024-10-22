from django.db import models
from django.conf import settings

class Property(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='properties/')
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add=True)
    noRooms = models.IntegerField()
    noBath = models.IntegerField()
    size = models.FloatField()  # Size in square meters

    # to link property to the user who created it
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    
    class Meta:
        verbose_name_plural = "Properties"  # to set correct plural name

    def __str__(self):
        return self.name
