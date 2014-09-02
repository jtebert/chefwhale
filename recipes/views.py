from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from models import Recipe, Box


def index(request):
    return render(request, 'recipes/index.html')


class RecipeList(generic.ListView):
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        """ List all recipes """
        return Recipe.objects.order_by('name')

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

class BoxList(generic.ListView):
    template_name = 'recipes/box_list.html'
    context_object_name = 'boxes'
    
    def get_queryset(self):
        """List all recipe boxes"""
        return Box.objects.order_by('name')