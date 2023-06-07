from django.shortcuts import render
from users.models import Student

# Create your views here.


def index(request):
    students=Student.objects.all()
    print(students)
    context={
        "students":students,
        "title": "customers",
    }
    return render(request, 'index.html',context=context)