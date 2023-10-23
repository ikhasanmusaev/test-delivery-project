from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from djangoProject.permissions import IsEmployee
from menu.models import FoodCategory, Food
from menu.serializers import CategorySerializer, FoodSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsEmployee]


class FoodsViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, IsEmployee]
