from django.db import models

class ListingUser(models.Model):
    TOPIC_CHOICES = (
        ('home buyer', 'Home Buyer'),
        ('renter', 'Renter'),
        ('home seller', 'Home Seller'),
        ('home owner', 'Home Owner'),
        ('investor', 'Investor'),
        ('general industry', 'General Industry'),
    )

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    topic = models.CharField(max_length=30, choices=TOPIC_CHOICES)
    user_description = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
