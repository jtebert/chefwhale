from django import forms
from models import *
from django.utils.translation import ugettext as _
from django.forms.widgets import mark_safe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe