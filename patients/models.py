from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=6)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"
