from django.shortcuts import render,redirect
from django.contrib import messages

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
            crew = form.cleaned_data['crew']
            plane = form.cleaned_data['airplane']
            pilot = False
            for person in crew:
                if person.is_pilot:
                    if person.rating == plane.rating:
                        pilot = True
                    else:
                        messages.warning(request,"The plane rating and the pilot rating don't match!")
                else:
                    messages.warning(request,"You can't add a flight without a pilot!")
            if pilot:
                form.save()
                return redirect("flight listview")
            else:
                return render(request,'flight_new.html',{'form':form})
    else:
        form = FlightForm()
        return render(request,'flight_new.html',{'form':form})

def detail_view(request,id):
    if request.method == "POST":
        flight = Flight.objects.get(id=request.POST['id'])
        form = FlightForm(request.POST,instance=flight)
        if form.is_valid():
            crew = form.cleaned_data['crew']
            plane = form.cleaned_data['airplane']
            pilot = False
            for person in crew:
                if person.is_pilot:
                    if person.rating == plane.rating:
                        pilot = True
                    else:
                        messages.warning(request,"The plane rating and the pilot rating don't match!")
                else:
                    messages.warning(request,"You can't add a flight without a pilot!")
            if pilot:
                form.save()
                return redirect("flight detailview",id=flight.pk)
            else:
                return render(request,'flight_detail.html',{'form':form,'flight':flight})
    else:
        flight = Flight.objects.get(id=id)
        form = FlightForm(instance=flight)
        return render(request,'flight_detail.html',{'form':form,'flight':flight})

def delete(request,id):
    flight = Flight.objects.get(id=id)
    flight.delete()
    return redirect("flight listview")