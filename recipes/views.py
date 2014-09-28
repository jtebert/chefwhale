from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404

from models import Recipe, Box
from utils import profile_from_request
from forms import *


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


@login_required
def recipe_list(request):
    profile = profile_from_request(request)
    recipes = Recipe.objects.filter(user=profile).order_by('name')

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

    # TODO: Correct response based on privacy settings
    
    return render(
        request, 'recipes/recipe_detail.html',
        {
            'recipe': recipe,
            'profile': profile,
        }
    )


@login_required
def recipe_add(request):
    profile = profile_from_request(request)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = profile_from_request(request)
            ingredient_form = IngredientFormSet(request.POST, prefix='ingredient', instance=recipe)
            instruction_form = InstructionFormSet(request.POST, prefix='instruction', instance=recipe)
            if ingredient_form.is_valid() and instruction_form.is_valid():
                recipe = recipe.save()
                ingredient_form.save()
                instruction_form.save()
                messages.success(request, _("Recipe added."))
                return HttpResponseRedirect(reverse("recipes:recipe_list"))
    else:  # GET
        recipe_form = RecipeForm()
        ingredient_form = IngredientFormSet(prefix='ingredient', instance=Recipe())
        instruction_form = InstructionFormSet(prefix='instruction', instance=Recipe())

    return render(
        request, 'recipes/recipe_add.html',
        {
            'profile': profile,
            'recipe_form': recipe_form,
            'ingredient_form': ingredient_form,
            'instruction_form': instruction_form,
        }
    )


@login_required
def recipe_edit(request, pk):
    # check if correct user
    profile = profile_from_request(request)
    recipe = get_object_or_404(Recipe, pk=pk)
    if not profile == recipe.user:
        raise PermissionDenied
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = profile_from_request(request)
            ingredient_form = IngredientFormSet(request.POST, prefix='ingredient', instance=recipe)
            instruction_form = InstructionFormSet(request.POST, prefix='instruction', instance=recipe)
            if ingredient_form.is_valid() and instruction_form.is_valid():
                recipe = recipe.save()
                ingredient_form.save()
                instruction_form.save()
                messages.success(request, _("Recipe added."))
                return HttpResponseRedirect(reverse("recipes:recipe_list"))
    else:  # GET
        recipe_form = RecipeForm(instance=recipe)
        ingredient_form = IngredientFormSet(prefix='ingredient', instance=recipe)
        instruction_form = InstructionFormSet(prefix='instruction', instance=recipe)

    return render(
        request, 'recipes/recipe_add.html',
        {
            'profile': profile,
            'recipe_form': recipe_form,
            'ingredient_form': ingredient_form,
            'instruction_form': instruction_form,
        }
    )


@login_required
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

    # TODO: Correct response based on privacy settings

    return render(
        request, 'recipes/box_detail.html',
        {
            'box': box,
            'profile': profile,
        }
    )