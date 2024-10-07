from rest_framework.routers import DefaultRouter
from .views import ListingUserViewSet

router = DefaultRouter()
router.register(r'listing_users', ListingUserViewSet, basename='listing_users')

urlpatterns = router.urls
