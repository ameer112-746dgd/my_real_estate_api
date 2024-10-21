from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            "firstname": "Test",
            "lastname": "User",
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpass123"
        }
    
    def test_register_user(self):
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_login_user(self):
        self.client.post(reverse('register'), self.user_data)
        response = self.client.post(reverse('login'), {
            "email": self.user_data["email"],
            "password": self.user_data["password"]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_list(self):
        self.client.post(reverse('register'), self.user_data)
        self.client.login(email=self.user_data["email"], password=self.user_data["password"])
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_detail(self):
        self.client.post(reverse('register'), self.user_data)
        user = User.objects.first()
        self.client.login(email=self.user_data["email"], password=self.user_data["password"])
        response = self.client.get(reverse('user-detail', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
