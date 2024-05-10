from django.forms import ModelForm
from CitiesModule.models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = "__all__"