from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ListingUser
from .serializers import ListingUserSerializer

class ListingUserViewSet(viewsets.ModelViewSet):
    queryset = ListingUser.objects.all()
    serializer_class = ListingUserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Listing User created successfully!',
            'data': response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Listing User updated successfully!',
            'data': response.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # Check if user is an admin
        if request.user.is_active and request.user.role == 'admin':
            super().destroy(request, *args, **kwargs)
            return Response({
                'message': 'Listing User deleted successfully!'
            }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                'message': 'You do not have permission to delete users.'
            }, status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Listing Users retrieved successfully!',
            'data': response.data
        }, status=status.HTTP_200_OK)
