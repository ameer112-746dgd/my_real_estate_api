from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    Custom permission to only allow users with 'admin' role to delete.
    """
    def has_permission(self, request, view):
        # Allow access if the user is authenticated and has the 'admin' role
        return request.user.is_authenticated and request.user.role.lower() == 'admin'
