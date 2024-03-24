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
        
class IsAdminOrNothing (permissions.BasePermission):
    """
    Custom permission to only allow admin users to get list of users.
    """
    def has_permission(self, request, view):
        # Only allow the request if the user is an admin
        return request.user and request.user.is_authenticated and request.user.is_staff

class IsAdminOrSelf (permissions.BasePermission):
    """
    Custom permission to only allow users to see their own profile, and admins to see any profile.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Permissions are only allowed to the owner of the profile or admins.
        return obj == request.user or request.user.is_staff