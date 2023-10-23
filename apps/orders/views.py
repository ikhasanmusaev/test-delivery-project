from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from djangoProject.permissions import IsClient, IsEmployee
from orders.models import Address, Order
from orders.serializers import AddressSerializer, OrderSerializer


class AddressViewSet(ModelViewSet):  # vaqtdan yutish uchun modelviewset ishlatildi
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, ]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsClient()]
        if self.request.method in ['PUT', 'PATCH'] or self.action == 'list':
            return [(IsAuthenticated & IsEmployee & ~IsClient)()]
        return super().get_permissions()
