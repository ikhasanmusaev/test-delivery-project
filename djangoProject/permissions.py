from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

employee_roles = {'server', 'admin'}


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_superuser)


class IsEmployee(permissions.BasePermission):  # admin or server
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        user_roles = set(user.role.values_list('unique_name', flat=True))

        if employee_roles.intersection(user_roles):
            return True

        return False


class IsClient(permissions.BasePermission):  # clients
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        user_roles = list(user.role.values_list('unique_name', flat=True))

        if 'client' in user_roles:
            return True

        return False
