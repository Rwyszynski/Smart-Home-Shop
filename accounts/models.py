from django.db import models
from shop.views import *
from accounts.views import *
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
