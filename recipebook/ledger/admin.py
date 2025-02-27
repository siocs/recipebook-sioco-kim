from django.contrib import admin

from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class TaskInline(admin.TabularInline):
    model = RecipeIngredient
    
class TaskGroupAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [TaskInline, ]

class TaskAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('ingredient', 'recipe')
    list_display = ('ingredient', 'quantity', 'recipe')
    list_filter = ('recipe', 'ingredient')

admin.site.register(Recipe, TaskGroupAdmin)
admin.site.register(RecipeIngredient, TaskAdmin)