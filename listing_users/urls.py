from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingUserViewSet 

router = DefaultRouter()
router.register(r'listing_users', ListingUserViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
