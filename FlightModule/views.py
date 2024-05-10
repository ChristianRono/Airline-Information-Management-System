from django.shortcuts import render,redirect

from FlightModule.models import Flight
from FlightModule.forms import FlightForm

# Create your views here.

def index(request):
    flights = Flight.objects.all()

    return render(request,'flight_listview.html',{'flights':flights})

def add_new(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flight listview")
    else:
        form = FlightForm()
        return render(request,'flight_new.html',{'form':form})

def detail_view(request,id):
    if request.method == "POST":
        flight =Flight.objects.get(id=request.POST['id'])
        form = FlightForm(request.POST,instance=flight)
        if form.is_valid():
            form.save()
            return redirect("flight detailview",id=flight.pk)
    else:
        flight = Flight.objects.get(id=id)
        form = FlightForm(instance=flight)
        return render(request,'flight_detail.html',{'form':form,'flight':flight})

def delete(request,id):
    flight = Flight.objects.get(id=id)
    flight.delete()
    return redirect("flight listview")