from django.shortcuts import render
from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'ledger/recipes_list.html', ctx)

def recipe_detail(request, pk):
    ctx = {'recipe': Recipe.objects.get(pk=pk)}
    return render(request, 'ledger/recipe_detail.html', ctx)

