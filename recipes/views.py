from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import AnonymousUser

from models import Recipe, Box


def index(request):
    print request.user
    if isinstance(request.user, AnonymousUser):
        profile = None
    else:
        profile = request.user.get_profile()
    return render(
        request, 'recipes/index.html',{'profile': profile})


def recipe_list(request):
    recipes = Recipe.objects.order_by('name')
    profile = request.user.get_profile()
    
    return render(
        request, 'recipes/recipe_list.html',
        {
            'recipes': recipes,
            'profile': profile,
        }
    )

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    profile = request.user.get_profile()
    
    return render(
        request, 'recipes/recipe_detail.html',
        {
            'recipe': recipe,
            'profile': profile,
        }
    )

class BoxList(generic.ListView):
    template_name = 'recipes/box_list.html'
    context_object_name = 'boxes'
    
    def get_queryset(self):
        """List all recipe boxes"""
        return Box.objects.order_by('name')


def box_list(request):
    boxes = Box.objects.order_by('name')
    profile = request.user.get_profile()
    
    return render(
        request, 'recipes/box_list.html',
        {
            'boxes': boxes,
            'profile': profile,
        }
    )