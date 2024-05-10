from django import forms
from AirplaneModule.models import Airplane

class AirplaneForm(forms.ModelForm):

    class Meta:
        model = Airplane
        fields = ["id","numser","manufacturer","model","rating"]