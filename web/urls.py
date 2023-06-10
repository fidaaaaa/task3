from django.urls import path,include

from web import views


app_name="web"


urlpatterns = [
    path('<int:id>', views.single, name = 'single'),
    path('', views.index, name = 'index'),
    
]