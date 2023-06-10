from django.shortcuts import render ,reverse

from django.contrib.auth import authenticate , login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from users.forms import UserForm
from users.models import Student

# Create your views here.

def sign(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        

        if form.is_valid():
            instance = form.save(commit=False)
            user = User.objects.create_user(
                username=instance.full_name,
                password=instance.password,
            )

            student=Student.objects.create(
                number=user.id,
                full_name=user.username,
                phone=instance.phone,
                email=instance.email,
                user=user,
            )

            user = authenticate(request, username=instance.full_name, password=instance.password)
            auth_login(request,user)
            url=f'/{student.number}'
            return HttpResponseRedirect(url)

    form = UserForm()
    context={
        "title":"Sign Up",
        "form" : form,
        

    }
    
    return render(request, 'auth/sign.html',context=context)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request,user)
                url=f'/{user.pk}'
                return HttpResponseRedirect(url)

            
        context = {
            "title":"Login",
            "error" : True,
            "message": "invalid Username or Password"
        }
        return render(request,"auth/login.html",context=context) 
    else:
        context = {
            "title":"Login"
        }
        return render(request,"auth/login.html",context=context)