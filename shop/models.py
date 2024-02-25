from asyncio import protocols
from django.db import models
from django.forms import CharField


class Products(models.Model):
    brand = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=32, blank=False, unique=True)
    voltage = models.PositiveSmallIntegerField(default=24)
    power = models.PositiveSmallIntegerField(blank=True)
    current = models.DecimalField(max_digits=6, decimal_places=1, blank=True)
    protocol = models.CharField(max_length=10, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.model)
