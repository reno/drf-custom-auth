from rest_framework import permissions


class UserAccessPermission(permissions.BasePermission):
    """
    Object-level permission to only allow the user to access and modify its data.
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
