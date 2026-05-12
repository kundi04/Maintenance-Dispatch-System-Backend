from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'manager'


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'staff'


class IsResident(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'resident'
