from django.urls import path
from .views import recipes_list, recipe_1, recipe_2, ingredient_detail

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipe/1', recipe_1, name='recipe-1'),
    path('recipe/2', recipe_2, name='recipe-2'),
    path('ingredient/<int:pk>', ingredient_detail, name='ingredient-detail')
]

app_name = "ledger"