# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics
# from .models import User
# from .serializers import UserSerializer

# class UserListCreateView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# users/views.py

from rest_framework import viewsets
from .models import User  # Ensure the User model is correctly imported
from .serializers import UserSerializer  # Ensure the serializer is correctly imported

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
