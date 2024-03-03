from django.db import models
from orders.views import *
from shop.views import *
from accounts.views import *


class Client(models.Model):
    user = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
