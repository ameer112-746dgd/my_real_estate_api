from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer
import os

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]  # Users must be authenticated to access

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "Properties retrieved successfully!",
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
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
        # Check if the user is active and has the 'admin' role
        if request.user.is_active and request.user.role.lower() == 'admin':  # Use lower() to match the role
            property_instance = self.get_object()
            image_path = property_instance.image.path  # Get the path of the image
            
            # Debugging info
            print(f"Deleting property: {property_instance.id}, Image Path: {image_path}")
            
            property_instance.delete()  # Delete the property
            if os.path.exists(image_path):  # Check if the image file exists
                os.remove(image_path)  # Delete the image file
                print("Image deleted successfully.")
            else:
                print("Image not found, deletion skipped.")
            
            return Response({'message': 'Property deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You do not have permission to delete properties.'}, status=status.HTTP_403_FORBIDDEN)
