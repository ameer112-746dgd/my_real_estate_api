from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    firstname = models.CharField(max_length=50)  # Add firstname field
    lastname = models.CharField(max_length=50)   # Add lastname field
    username = models.CharField(max_length=150, unique=True, default='default_user')  # Add default value
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = ['firstname', 'lastname']  # Add required fields
    firstname = models.CharField(max_length=50, null=True, blank=True)  # Allow null values
    lastname = models.CharField(max_length=50, null=True, blank=True)   # Allow null values
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
