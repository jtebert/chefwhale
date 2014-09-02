from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from models import Recipe


def index(request):
    return render(request, 'recipes/index.html')


class RecipeListView(generic.ListView):
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        """ List all recipes """
        print Recipe.objects.all()
        return Recipe.objects.order_by('name')

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

"""def BoxesList(generic.ListView):
    template_name = 'recipes/'"""