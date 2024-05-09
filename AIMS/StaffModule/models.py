from django.db import models

# Create your models here.

class Staff(models.Model):
    employee_number = models.IntegerField()
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    salary = models.IntegerField()
    CHOICES = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
    )
    rating = models.CharField(max_length=10,choices=CHOICES,blank=True)
    is_pilot = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.surname}, {self.name}"