from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated


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

class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admin users, or profile owners to view.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Permissions are only allowed to the owner of the profile or admins.
        return obj == request.user or request.user.is_staff