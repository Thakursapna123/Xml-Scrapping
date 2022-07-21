from django.core import serializers
from django.shortcuts import redirect, render
from .models import Person
from .forms import Personform
from django.contrib import messages
# Create your views here.
def create(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        mobile=request.POST['mobile']
        if Person.objects.filter(email=email).exists():
             messages.success(request, f'Email already exists')
        else:
            form=Person(first_name=first_name,last_name=last_name,email=email,address=address,mobile=mobile)
            form.save()
            messages.success(request, f'Record Insterted Successfully')
            return redirect("/")
    show_data=Person.objects.all().values()
    return render(request,"index.html",{'show_data':show_data})



def delete(request,id):
    a=Person.objects.filter(id=id)
    a.delete()
    messages.success(request, f'Record Deleted Successfully')
    return redirect("/")


def updaterecord(request,id):
    if request.method=="POST":
        email=request.POST['email']
        obj=Person.objects.get(id=id)
        form=Personform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record Updated Successfully')
            return redirect("/")
    else:
        obj=Person.objects.get(id=id)
        form=Personform(instance=obj)
    return render(request,"update.html",{'form':form})

# @csrf_exempt
# def edit(request):
#     id=request.POST['edit_id']
#     obj=Person.objects.filter(id=id).values()
#     print(obj)
#     # jsonData=serializers.serialize("json",obj)
#     return render(request,'index.html',{'formData':obj})
  
def edit_data(request,id):
    obj=Person.objects.get(id=id)
    show_data=Person.objects.all().values()
    return render(request,'index.html',{'update':obj,'show_data':show_data})

def update_item(request,id):
    obj=Person.objects.get(id=id)
    obj.first_name=request.POST['first_name']
    obj.last_name=request.POST['last_name']
    obj.email=request.POST['email']
    obj.address=request.POST['address']
    obj.mobile=request.POST['mobile']
    obj.save()
    messages.success(request, f'Record Updated Successfully')
    return redirect("/")

  
  
        



