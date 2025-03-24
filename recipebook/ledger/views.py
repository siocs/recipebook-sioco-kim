from .models import Recipe, RecipeIngredient, RecipeImage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RecipeForm, RecipeImageForm
from django.urls import reverse


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['ingredients'] = RecipeIngredient.objects.filter(
            recipe=self.object
            )
        return ctx
    

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class RecipeImageCreateView(CreateView):
    model = RecipeImage
    form_class = RecipeImageForm

    def form_valid(self, form):
        self.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        form.instance.recipe = self.recipe
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('ledger:recipe-detail', kwargs={'pk': self.recipe.pk})
