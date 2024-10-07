# from django.urls import path
# from .views import UserListCreateView

# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list-create'),
# ]


# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet  # Ensure this matches the class name in views.py

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated routes
]
