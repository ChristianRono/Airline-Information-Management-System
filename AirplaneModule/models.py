from django.db import models

# Create your models here.
class Airplane(models.Model):
    numser = models.IntegerField()
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    CHOICES = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
    )
    rating = models.CharField(max_length=10,choices=CHOICES)

    def __str__(self):
        return f"{self.manufacturer} {self.model} plane no:{str(self.numser)}, rating: {self.get_rating_display()}"