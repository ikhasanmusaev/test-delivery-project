from rest_framework import serializers

from menu.models import FoodCategory, Food


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = [
            'id',
            'title',
        ]


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'title',
            'category',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation
