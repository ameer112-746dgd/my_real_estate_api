# from django.urls import path
# from .views import BlogListCreateView

# urlpatterns = [
#     path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
# ]


# from django.urls import path
# from .views import BlogViewSet

# urlpatterns = [
#     path('blogs/', BlogViewSet.as_view({'get': 'list', 'post': 'create'}), name='blog-list-create'),
# ]


from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)  # Register the BlogViewSet

urlpatterns = router.urls
