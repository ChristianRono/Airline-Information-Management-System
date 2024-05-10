from django.shortcuts import render,redirect
from django.contrib import messages

from StaffModule.models import Staff
from StaffModule.forms import StaffForm

# Create your views here.

def index(request):
    staffs = Staff.objects.all().order_by('employee_number')

    return render(request,'staff_listview.html',{'staffs':staffs})

def add_new(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            is_pilot = form.cleaned_data['is_pilot']
            rating = form.cleaned_data['rating']

            if is_pilot:
                if rating:
                    form.save()
                    return redirect("staff listview")
                else:
                    messages.warning(request, "You can't add a pilot without a rating!")
                    return render(request, 'staff_new.html',{'form':form})
            else:
                if rating:
                    messages.warning(request, "Normal crew members don't have a rating!")
                    return render(request, 'staff_new.html',{'form':form})

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
            is_pilot = form.cleaned_data['is_pilot']
            rating = form.cleaned_data['rating']

            if is_pilot:
                if rating:
                    form.save()
                    return redirect("staff detailview",id=staff.pk)
                else:
                    messages.warning(request, "You can't add a pilot without a rating!")
                    return render(request, 'staff_detail.html',{'form':form})
            else:
                if rating:
                    messages.warning(request, "Normal crew members don't have a rating!")
                    return render(request, 'staff_detail.html',{'form':form})

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