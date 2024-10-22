from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can interact

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the author of the blog
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        # Only the original author or admin can update the blog
        if serializer.instance.author != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to edit this blog post.")
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'message': 'Blog post created successfully!',
                'blog': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response({
            'message': 'Blog post retrieved successfully!',
            'blog': serializer.data
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        blog = self.get_object()
        serializer = self.get_serializer(blog, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                'message': 'Blog post updated successfully!',
                'blog': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()  # Get the blog post to be deleted
        
        # Check if the user is active and has the 'admin' role
        if request.user.is_active and request.user.role.lower() == 'admin':
            blog.delete()  # Delete the blog post
            return Response({'message': 'Blog post deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'You do not have permission to delete blog posts.'}, status=status.HTTP_403_FORBIDDEN)
