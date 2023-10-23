from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orders.views import AddressViewSet, OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, 'orders')
router.register('address', AddressViewSet, 'addresses')

urlpatterns = [
    path('', include(router.urls)),
]
