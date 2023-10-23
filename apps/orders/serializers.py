from rest_framework import serializers

from menu.serializers import FoodSerializer
from orders.models import Address, Order
from users.serializers import UserPartialSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'title',
            'range_per_km',
        ]


class OrderSerializer(serializers.ModelSerializer):
    delivery_time_in_minutes = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'food',
            'status',
            'address',
            'delivery_time_in_minutes',
        ]

    def create(self, validated_data):
        validated_data['client'] = self.context['request'].user
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['address'] = AddressSerializer(instance.address).data
        representation['food'] = FoodSerializer(instance.food).data
        representation['client'] = UserPartialSerializer(instance.client).data
        return representation

    def get_delivery_time_in_minutes(self, obj):
        orders = Order.objects.filter(created_at__lt=obj.created_at, status=1).exclude(id=obj.id)
        orders_count = orders.count()
        travel_time = obj.address.range_per_km * 3
        return (orders_count // 4 * 5) + travel_time + 5

    def get_status(self, obj):
        return list(filter(lambda status: status[0] == obj.status, self.Meta.model.STATUSES))[0][1]
