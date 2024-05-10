from django.forms import ModelForm
from FlightModule.models import Flight
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"