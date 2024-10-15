# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Blog
# from .serializers import BlogSerializer
# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Blog  # Assuming you have a Blog model

# def home_view(request):
#     return render(request, 'home.html')
# def blog_list(request):
#     return render(request, 'blog_list.html')
# class BlogListView(ListView):
#     model = Blog
#     template_name = 'blogs/blog_list.html'  # Your template file for the blog list
#     context_object_name = 'blogs'  # This will be the context variable in the template


# def blog_list(request):
#     return render(request, 'blog_list.html')  # Rendering the centralized template


# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

#     # Override create method for POST (Create) request
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'message': 'Blog post created successfully!',
#                     'blog': serializer.data
#                 },
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Override retrieve method for GET (Retrieve) request
#     def retrieve(self, request, *args, **kwargs):
#         blog = self.get_object()
#         serializer = self.get_serializer(blog)
#         return Response(
#             {
#                 'message': 'Blog post retrieved successfully!',
#                 'blog': serializer.data
#             }
#         )

#     # Override update method for PUT (Update) request
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         blog = self.get_object()
#         serializer = self.get_serializer(blog, data=request.data, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {
#                     'message': 'Blog post updated successfully!',
#                     'blog': serializer.data
#                 }
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Override destroy method for DELETE request
#     def destroy(self, request, *args, **kwargs):
#         blog = self.get_object()
#         blog.delete()
#         return Response(
#             {'message': 'Blog post deleted successfully!'},
#             status=status.HTTP_204_NO_CONTENT
#         )


from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.generic import ListView
from .models import Blog
from .serializers import BlogSerializer

# Home view
def home_view(request):
    return render(request, 'home.html')

# Blog list view
def blog_list(request):
    return render(request, 'blog_list.html')

# Blog list using class-based view
class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'

# Blog detail view to display an individual blog
def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

# DRF ViewSet for API
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

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
