from django.db import models
from django.contrib.auth.models import Group


class Role(models.Model):
    name = models.JSONField(default=dict, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='roles', blank=True)
    unique_name = models.CharField(max_length=125, unique=True)

    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.unique_name) + f' - {self.name["uz"]}'


# Employee lar admin paneldan qo'shiladi

class UserRole(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    role = models.ForeignKey('users.Role', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.role.unique_name)
