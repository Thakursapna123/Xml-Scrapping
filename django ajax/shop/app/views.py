from audioop import add
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def add_student(request):
    return render(request,"show.html")

























def index(request):
    form=StudentForm()
    obj=Student.objects.all().values()

    return render(request,"index.html",{'form':form,'obj':obj})

@csrf_exempt
def show(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            modify=request.POST['modify']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            age=request.POST['age']
            address=request.POST['address']
            city=request.POST['city']
            if (modify ==''):
                obj=Student(first_name=first_name,last_name=last_name,age=age,city=city,address=address)
                obj.save()
                response = {'status': 'success', 'message': 'Record inserted'}
                return JsonResponse(response)
            else:
                obj=Student(id=modify,first_name=first_name,last_name=last_name,age=age,city=city,address=address)
                obj.save()
                response = {'status': 'success', 'message': 'Record Updated'}
                return JsonResponse(response)
 
            
          
        else:
            response = {'status': 'failed', 'message': 'not'}
            return JsonResponse(response)

def del_student(request):
    id=request.GET['id']
    print(id)
    obj=Student.objects.filter(id=id)
    obj.delete()
    return JsonResponse({'status':'success','message':'Record delete successfully'})


@csrf_exempt
def edit_student(request):
    if request.method=="POST":
        id=request.POST['id']
        obj=Student.objects.get(id=id)
        data={"id":obj.id,"first_name":obj.first_name,"last_name":obj.last_name,"age":obj.age,"city":obj.city}
        return JsonResponse(data)

