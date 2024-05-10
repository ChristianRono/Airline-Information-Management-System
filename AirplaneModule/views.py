from django.shortcuts import render,redirect

from AirplaneModule.models import Airplane

# Create your views here.

def index(request):
    airplanes = Airplane.objects.all()

    return render(request,'airplane_listview.html',{'airplanes':airplanes})

def detail_view(request,id):
    airplane = Airplane.objects.get(id=id)

    return render(request,'airplane_detail.html',{'airplane':airplane})

def delete(request,id):
    airplane = Airplane.objects.get(id=id)
    print(airplane.delete())
    return redirect("airplane listview")