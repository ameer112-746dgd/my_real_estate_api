from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
            serializer.save()
            return Response({
                'message': 'Blog post updated successfully!',
                'blog': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.delete()
        return Response({'message': 'Blog post deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
