from django.db import models
from orders.models import Order


class Result(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
