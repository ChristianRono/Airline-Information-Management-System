from django.shortcuts import render,redirect

from StaffModule.models import Staff
from StaffModule.forms import StaffForm

# Create your views here.

def index(request):
    staffs = Staff.objects.all()

    return render(request,'staff_listview.html',{'staffs':staffs})

def add_new(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff listview")
    else:
        form = StaffForm()
        return render(request,'staff_new.html',{'form':form})

def detail_view(request,id):
    if request.method == "POST":
        staff =Staff.objects.get(id=request.POST['id'])
        form = StaffForm(request.POST,instance=staff)
        if form.is_valid():
            form.save()
            return redirect("staff detailview",id=staff.pk)
    else:
        staff = Staff.objects.get(id=id)
        form = StaffForm(instance=staff)
        return render(request,'staff_detail.html',{'form':form,'staff':staff})

def delete(request,id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect("staff listview")