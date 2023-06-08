from django import forms
from users.models import Student
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ["full_name","email","password","phone"]
        widgets = {
            "password" : forms.widgets.PasswordInput()
        }