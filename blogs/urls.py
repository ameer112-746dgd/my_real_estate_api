from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)  # Register the BlogViewSet

urlpatterns = router.urls
