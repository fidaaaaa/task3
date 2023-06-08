from django import forms
from food.models import Food

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields=["breakfast","lunch","tea","dinner"]

        widgets = {
            "breakfast":forms.TextInput(attrs={'required':'false',"placeholder":"Type Breakfast"}),
            "lunch":forms.TextInput(attrs={'required':'false',"placeholder":"Type Lunch"}),
            "tea":forms.TextInput(attrs={'required':'false',"placeholder":"Type Tea"}),
            "dinner":forms.TextInput(attrs={'required':'false',"placeholder":"Type Dinner"}),
        }
