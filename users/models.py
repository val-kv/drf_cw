from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = models.CharField(max_length=12, null=True, blank=True)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    class Meta:
        swappable = 'AUTH_USER_MODEL'
