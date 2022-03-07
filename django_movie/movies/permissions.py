from rest_framework import permissions


class IsAuthorEntryOrAdmin(permissions.BasePermission):
    """Автор комментария или админимтратор"""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or bool(request.user and request.user.is_staff)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Просмотр или администратор"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)