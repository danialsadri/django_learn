from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "دسترسی نداری که این پست رو تغییر بدی"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author.user == request.user


class IsAdminOrSuperUser(BasePermission):
    message = "..."

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_staff
            or request.user
            and request.user.is_superuser
        )
