from django import forms
from django.forms.models import inlineformset_factory
from models import *
from django.utils.translation import ugettext as _
from django.forms.widgets import mark_safe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'image', 'recipe_yield', 'time_active', 'time_total', 'description', 'source')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':_("Recipe Name"),}),
            'description': forms.Textarea(attrs={'placeholder': _("Recipe Description")})
        }


IngredientFormSet = inlineformset_factory(Recipe, Ingredient)
InstructionFormSet = inlineformset_factory(Recipe, Instruction)