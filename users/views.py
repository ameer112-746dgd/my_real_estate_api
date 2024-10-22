from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from .permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow anyone to login

    def post(self, request):
        email = request.data.get('email')  # Get the email from the request
        password = request.data.get('password')  # Get the password from the request
        
        # Authenticate using email and password
        user = authenticate(email=email, password=password)

        if user is not None:
            access_token = AccessToken.for_user(user)
            return Response({"token": str(access_token)}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.permission_classes = [IsAdminUser]
        user = get_object_or_404(User, pk=pk)
        self.check_permissions(request)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get(self, request):
        users = User.objects.all()  # Retrieve all users
        serializer = UserSerializer(users, many=True)  # Serialize the user data
        return Response(serializer.data)

