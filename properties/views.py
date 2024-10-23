import os
from .models import Property
from .permissions import IsAdminUserRole
from rest_framework import viewsets, status
from .serializers import PropertySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]  # Ensure users are authenticated to interact

    def perform_create(self, serializer):
        # To set the user who created the property
        serializer.save(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "Properties retrieved successfully!",
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        
        self.permission_classes = [IsAdminUserRole]
        self.check_permissions(request)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            property_instance = serializer.save()
            return Response({
                "message": "Property created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "message": "Property retrieved successfully!",
            "data": serializer.data
        })

    def update(self, request, *args, **kwargs):
        
        self.permission_classes = [IsAdminUserRole]
        self.check_permissions(request)
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            property_instance = serializer.save()
            return Response({
                "message": "Property updated successfully!",
                "data": serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Apply custom permission to ensure only admins can delete properties
        self.permission_classes = [IsAdminUserRole]
        self.check_permissions(request)

        property_instance = self.get_object()  # To get the property instance to be deleted
        image_path = property_instance.image.path  # To get the path of the associated image

        property_instance.delete()  # Delete the property instance

        # Check if the image file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)
            print("Image deleted successfully.")
        else:
            print("Image not found, deletion skipped.")
        
        return Response({'message': 'Property deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
