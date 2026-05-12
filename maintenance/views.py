from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'manager':
            return MaintenanceRequest.objects.all()

        elif user.role == 'staff':
            return MaintenanceRequest.objects.filter(assigned_to=user)

        return MaintenanceRequest.objects.filter(resident=user)

    def perform_create(self, serializer):
        serializer.save(resident=self.request.user)

    def perform_update(self, serializer):
        user = self.request.user
        instance = self.get_object()

        if user.role == 'staff':
            serializer.save(assigned_to=instance.assigned_to)
        else:
            serializer.save()
