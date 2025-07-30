from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplyRequestViewSet

router = DefaultRouter()
router.register(r'requests', SupplyRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
