# from rest_framework import viewsets
# from .models import ListingUser
# from .serializers import ListingUserSerializer

# class ListingUserViewSet(viewsets.ModelViewSet):
#     queryset = ListingUser.objects.all()
#     serializer_class = ListingUserSerializer


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ListingUser
from .serializers import ListingUserSerializer

class ListingUserViewSet(viewsets.ModelViewSet):
    queryset = ListingUser.objects.all()
    serializer_class = ListingUserSerializer

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
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': 'Listing User deleted successfully!'
        }, status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'message': 'Listing Users retrieved successfully!',
            'data': response.data
        }, status=status.HTTP_200_OK)
