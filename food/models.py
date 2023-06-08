from django.db import models

class Day(models.Model):
    name=models.CharField(max_length=255)
    food = models.ManyToManyField("food.Food")

    def __str__(self):
        return self.name


class Food(models.Model):
    days=models.CharField(max_length=255,default="day1")
    breakfast=models.CharField(max_length=255)
    lunch=models.CharField(max_length=255)
    tea=models.CharField(max_length=255)
    dinner=models.CharField(max_length=255)
    
    # food_name=models.ForeignKey("food.Day",on_delete=models.CASCADE)

    def __str__(self):
        return self.days