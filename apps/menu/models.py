from django.db import models


class FoodCategory(models.Model):
    title = models.CharField(max_length=63)


class Food(models.Model):
    title = models.CharField(max_length=63)
    category = models.ForeignKey('FoodCategory', on_delete=models.CASCADE)
