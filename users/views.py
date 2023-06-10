from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from users.forms import UserForm
from users.models import Student

def sign(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            user = User.objects.create_user(
                username=instance.full_name,
                password=instance.password,
            )

            student = Student.objects.create(
                number=user.id,
                full_name=user.username,
                phone=instance.phone,
                email=instance.email,
                user=user,
            )

            user = authenticate(request, username=instance.full_name, password=instance.password)
            auth_login(request, user)
            url = f'/{student.number}'
            return HttpResponseRedirect(url)

    else:
        form = UserForm()

    context = {
        "title": "Sign Up",
        "form": form,
    }

    return render(request, 'auth/sign.html', context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")
            else:
                context={
                    "title": "Login",
                    "error":True,
                    "message": "Invalid username or password"
                }
                return render(request, 'users/login.html', context=context)