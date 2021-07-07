from rest_framework import permissions


class UserAccess(permissions.BasePermission):
    """
    Object-level permission to only allow the user to access and modify its data.
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class CreateOrAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_authenticated:
            return True
        elif request.method == 'POST':
            return True
        else:
            return False