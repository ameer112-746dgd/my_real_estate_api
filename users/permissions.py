from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'admin' role to delete users.
    """
    def has_permission(self, request, view):
        # Only allow DELETE requests from users with the 'admin' role
        if request.method == "DELETE":
            return request.user.is_authenticated and request.user.role == 'admin'
        return True
