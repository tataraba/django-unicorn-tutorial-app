from django.forms import ModelForm

from .models import Meal


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        required = ['name']
        labels = {
            "name": "Name",
            "main_dish": "Main dish",
            "side_dish": "Side dish",
            "desert": "Desert",
            "type_of_meal": "Type of meal",
        }