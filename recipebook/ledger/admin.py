from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine, RecipeImageInLine]
    list_display = ('name', 'author', 'created_on', 'update_on')


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('ingredient', 'recipe')
    list_display = ('ingredient', 'quantity', 'recipe')
    list_filter = ('recipe', 'ingredient')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage)
