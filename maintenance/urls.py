from rest_framework.routers import DefaultRouter
from .views import MaintenanceRequestViewSet

router = DefaultRouter()
router.register(r'requests', MaintenanceRequestViewSet, basename='requests')

urlpatterns = router.urls
