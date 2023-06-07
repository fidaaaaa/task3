from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls", namespace="web")),
    # path('food/', include("food.urls", namespace="food")),
    # path('users/', include("users.urls", namespace="users")),
]
