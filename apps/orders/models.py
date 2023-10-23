from django.db import models


class Order(models.Model):
    STATUSES = [
        (1, 'in_progress'),
        (2, 'at_courier'),
        (3, 'delivered'),
    ]

    food = models.ForeignKey('menu.Food', on_delete=models.PROTECT)
    client = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUSES,
                                 default=1)  # masalan yuborish uchun status o'zgartiriladi ofitsiant tomonidan

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class Address(models.Model):  # klient address tanlashi yoki qo'shish uchun
    title = models.CharField(max_length=255)
    range_per_km = models.IntegerField(default=1)
