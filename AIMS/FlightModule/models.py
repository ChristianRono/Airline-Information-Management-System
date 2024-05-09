from django.db import models
from CitiesModule.models import City
from PassengersModule.models import Passenger
from StaffModule.models import Staff
from AirplaneModule.models import Airplane

# Create your models here.

class Flight(models.Model):
    flight_number = models.IntegerField()
    origin = models.ForeignKey(City,related_name="origin",on_delete=models.DO_NOTHING)
    destination = models.ForeignKey(City,related_name="destination",on_delete=models.DO_NOTHING)
    stops = models.ManyToManyField(City)
    date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    passengers = models.ManyToManyField(Passenger)
    crew = models.ManyToManyField(Staff)
    airplane = models.ForeignKey(Airplane,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Flight No:{str(self.flight_number)} from {self.origin} to {self.destination}"
