from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    number = models.IntegerField()
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    user =models.OneToOneField("auth.User",on_delete=models.CASCADE)
    food = models.ManyToManyField("food.Food")
    


    def __str__(self):
        return self.full_name

