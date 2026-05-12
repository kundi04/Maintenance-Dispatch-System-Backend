from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer
from .permissions import IsManager, IsStaff, IsResident


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MaintenanceRequestSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsResident()]
        if self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsManager() | IsStaff()]
        if self.action == 'destroy':
            return [IsAuthenticated(), IsManager()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'resident':
            return MaintenanceRequest.objects.filter(resident=user)
        return MaintenanceRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(resident=self.request.user)

    def perform_update(self, serializer):
        user = self.request.user
        instance = self.get_object()

        if user.role == 'staff':
            serializer.save(
                assigned_to=instance.assigned_to
            )
        else:
            serializer.save()
