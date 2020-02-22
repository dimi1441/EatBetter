from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission allows owners to only use its objects(Create, Retrieve, Update, Delete).
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


