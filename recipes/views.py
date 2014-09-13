from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from models import Recipe, Box
from utils import profile_from_request


def index(request):
    profile = profile_from_request(request)

    return render(
        request, 'recipes/index.html', {
            'profile': profile
        }
    )


def about(request):
    profile = profile_from_request(request)

    """return render(
        request, 'recipe/about.html', {
            'profile': profile,
        }
    )"""

    return HttpResponse("About Page")


def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user).order_by('name')
    profile = profile_from_request(request)

    return render(
        request, 'recipes/recipe_list.html',
        {
            'recipes': recipes,
            'profile': profile,
        }
    )


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    profile = profile_from_request(request)
    
    return render(
        request, 'recipes/recipe_detail.html',
        {
            'recipe': recipe,
            'profile': profile,
        }
    )


def recipe_add(request):
    profile = profile_from_request(request)

    return render(
        request, 'recipes/recipe_add.html',
        {
            'profile': profile,
        }
    )


def box_list(request):
    boxes = Box.objects.order_by('name')
    profile = profile_from_request(request)
    
    return render(
        request, 'recipes/box_list.html',
        {
            'boxes': boxes,
            'profile': profile,
        }
    )


def box_detail(request, pk):
    box = Box.objects.get(pk=pk)
    profile = profile_from_request(request)

    return render(
        request, 'recipes/box_detail.html',
        {
            'box': box,
            'profile': profile,
        }
    )