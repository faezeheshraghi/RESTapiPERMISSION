from rest_framework.permissions import BasePermission, SAFE_METHODS,IsAuthenticated


class IsIrani(IsAuthenticated):

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.irani
