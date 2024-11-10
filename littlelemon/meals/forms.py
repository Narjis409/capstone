from django import forms
from .models import Meals

class MealsForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ['name', 'description', 'price', 'available']

