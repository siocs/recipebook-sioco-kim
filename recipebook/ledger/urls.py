from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipes-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add')
]

app_name = "ledger"
