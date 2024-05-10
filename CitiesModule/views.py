from django.shortcuts import render,redirect

from CitiesModule.models import City
from CitiesModule.forms import CityForm

# Create your views here.

def index(request):
    cities = City.objects.all()

    return render(request,'city_listview.html',{'cities':cities})

def add_new(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("city listview")
    else:
        form = CityForm()
        return render(request,'city_new.html',{'form':form})

def detail_view(request,id):
    if request.method == "POST":
        city =City.objects.get(id=request.POST['id'])
        form = CityForm(request.POST,instance=city)
        if form.is_valid():
            form.save()
            return redirect("city detailview",id=city.pk)
    else:
        city = City.objects.get(id=id)
        form = CityForm(instance=city)
        return render(request,'city_detail.html',{'form':form,'city':city})

def delete(request,id):
    city = City.objects.get(id=id)
    city.delete()
    return redirect("city listview")