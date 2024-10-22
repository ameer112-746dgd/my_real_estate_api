from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)  # non-nullable
    # username = models.CharField(max_length=150, unique=True, null=True)  # Allow null temporarily
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Store roles in lowercase
    ROLE_CHOICES = (('admin', 'Admin'), ('user', 'User'))
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()  # Use the CustomUserManager

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        # Normalize the role to lowercase before saving
        if self.role:
            self.role = self.role.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    