from django.shortcuts import render,redirect

from AirplaneModule.models import Airplane
from AirplaneModule.forms import AirplaneForm

# Create your views here.

def index(request):
    airplanes = Airplane.objects.all()

    return render(request,'airplane_listview.html',{'airplanes':airplanes})

def add_new(request):
    if request.method == "POST":
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("airplane listview")
    else:
        form = AirplaneForm()
        return render(request,'airplane_new.html',{'form':form})

def detail_view(request,id):
    if request.method == "POST":
        airplane =Airplane.objects.get(id=request.POST['id'])
        form = AirplaneForm(request.POST,instance=airplane)
        if form.is_valid():
            form.save()
            return redirect("airplane detailview",id=airplane.pk)
    else:
        airplane = Airplane.objects.get(id=id)
        form = AirplaneForm(instance=airplane)
        return render(request,'airplane_detail.html',{'form':form,'airplane':airplane})

def delete(request,id):
    airplane = Airplane.objects.get(id=id)
    airplane.delete()
    return redirect("airplane listview")