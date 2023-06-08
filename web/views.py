from django.shortcuts import render,get_object_or_404
from users.models import Student
from food.models import Day , Food


def index(request):
    students=Student.objects.all()
    print(students)
    context={
        "students":students,
        "title": "customers",
    }
    return render(request, 'index.html',context=context)

def single(request,id):
    instances = get_object_or_404(Student.objects.filter(number=id))
    days=Day.objects.all()
    foods=instances.food.all

    sort = request.GET.get("sort")


    context = {
        "instances" : instances ,
        "days" : days, 
        "title": instances.full_name,
        "foods": foods,

    }
    return render (request,"item.html",context=context) 