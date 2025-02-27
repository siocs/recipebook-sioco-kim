from django.urls import path
from .views import recipes_list, recipe_detail

urlpatterns = [
    path('recipes/list', recipes_list, name='recipes-list'),
    path('recipe/<int:pk>', recipe_detail, name='recipe-detail')
]

app_name = "ledger"
