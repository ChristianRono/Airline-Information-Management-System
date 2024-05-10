from django.forms import ModelForm

from StaffModule.models import Staff

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"