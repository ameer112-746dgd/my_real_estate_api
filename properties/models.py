from django.db import models
from django.conf import settings

class Property(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('NGN', 'Naira'),
    ]

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='properties/')
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    createdAt = models.DateTimeField(auto_now_add=True)
    noRooms = models.IntegerField()
    noBath = models.IntegerField()
    size = models.FloatField()

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return f'{self.name} - {self.currency} {self.price}'
