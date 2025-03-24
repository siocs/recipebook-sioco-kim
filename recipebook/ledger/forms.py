from django import forms
from .models import Recipe, RecipeImage
from django.forms.widgets import ClearableFileInput


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['description', 'image']
