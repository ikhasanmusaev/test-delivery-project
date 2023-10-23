from django.urls import include, path
from rest_framework.routers import DefaultRouter

from menu.views import CategoriesViewSet, FoodsViewSet

router = DefaultRouter()
router.register('categories', CategoriesViewSet, 'categories')
router.register('foods', FoodsViewSet, 'foods')

urlpatterns = [
    path('', include(router.urls)),
]
