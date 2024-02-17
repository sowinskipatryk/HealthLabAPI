from django.db import models
from patients.models import Patient


class Order(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
