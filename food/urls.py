from django.urls import path,include
from food import views



app_name="food"


urlpatterns = [
    path('add_food/<int:pk>', views.add_food, name = 'add_food'),
    
]