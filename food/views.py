from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponseRedirect

from food.models import Day,Food
from users.models import Student

from food.form import FoodForm

# Create your views here.
def add_food (request,pk):
    
    if request.method == 'POST':

        form = FoodForm(request.POST)
        student=Student.objects.get(number=request.user.id)

        day_name=get_object_or_404(Day.objects.filter(id=pk))

        if form.is_valid():
            instance=form.save(commit=False)

            foods,created=Food.objects.get_or_create(
                days=day_name,
                breakfast=instance.breakfast,
                lunch=instance.lunch,
                tea=instance.breakfast,
                dinner=instance.dinner,
            )

            day_name.food.add(foods)


            
            student.food.add(foods)
            url=f'/{request.user.id}'
            return HttpResponseRedirect(url)
        else:
            
            context={
                "title" :"Food Ordering",
                "error" : True,
                "message": "Error"
            }
            return render(request, 'add_food.html',context=context)

            
    else:
        form = FoodForm
        context= {
            "title" : "Food Ordering",
            "form" : form

        }
        return render(request, 'add_food.html',context=context)

