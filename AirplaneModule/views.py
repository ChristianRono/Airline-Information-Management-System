from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView

from AirplaneModule.models import Airplane

# Create your views here.

class AirplaneListView(ListView):
    model = Airplane
    context_object_name = "airplanes"
    template_name = "airplane_listview.html"

class AirplaneDetailView(DetailView):
    model = Airplane

def delete(request,id):
    airplane = Airplane.objects.get(id=id)
    print(airplane.delete())
    return redirect("airplane listview")