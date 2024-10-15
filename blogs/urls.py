from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
from .views import home_view
from . import views

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)  # Register the BlogViewSet

urlpatterns = router.urls
# blogs/urls.py

from django.urls import path
from .views import BlogListView  # Make sure to import the view

urlpatterns = [
   path('', views.blog_list, name='blog_list'),
   path('', home_view, name='home'),
   path('<int:blog_id>/', views.blog_detail_view, name='blog_detail'), 
]
