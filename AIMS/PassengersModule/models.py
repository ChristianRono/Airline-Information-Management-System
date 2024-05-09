from django.db import models

# Create your models here.

class Passenger(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.surname}, {self.name}"