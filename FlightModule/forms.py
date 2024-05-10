from django.forms import ModelForm
from FlightModule.models import Flight


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"