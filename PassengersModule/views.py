from django.shortcuts import render,redirect

from PassengersModule.models import Passenger
from PassengersModule.forms import PassengerForm

# Create your views here.

def index(request):
    passengers = Passenger.objects.all()

    return render(request,'passenger_listview.html',{'passengers':passengers})

def add_new(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("passenger listview")
    else:
        form = PassengerForm()
        return render(request,'passenger_new.html',{'form':form})

def detail_view(request,id):
    if request.method == "POST":
        passenger =Passenger.objects.get(id=request.POST['id'])
        form = PassengerForm(request.POST,instance=passenger)
        if form.is_valid():
            form.save()
            return redirect("passenger detailview",id=passenger.pk)
    else:
        passenger = Passenger.objects.get(id=id)
        form = PassengerForm(instance=passenger)
        return render(request,'passenger_detail.html',{'form':form,'passenger':passenger})

def delete(request,id):
    passenger = Passenger.objects.get(id=id)
    passenger.delete()
    return redirect("passenger listview")