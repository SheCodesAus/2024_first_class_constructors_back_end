from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit it.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # The method is a safe method
            return True
        else:
            # The method isn't a safe method
            # Only allow it if the user is an admin
            return request.user.is_staff
        
class IsAdminOrSelf (permissions.BasePermission):
    """
    Custom permission to only allow admin to get list of users,
    registered users to view their own profile, and
    allow new users to sign in.
    """
    def has_object_permission(self, request, view, obj):
        # If the request method is safe, only allow it if the user is an admin
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff
        # Allow POST requests if the user is not authenticated
        if not request.user.is_authenticated and request.method == 'POST':
            return True
        # If the request method is unsafe, only allow it if the user is the same as the object
        return obj == request.user or request.user.is_staff