from django.contrib import admin
from recipes.models import *

class IngredientInline(admin.StackedInline):
    model = Ingredient

class InstructionInline(admin.StackedInline):
    model = Instruction

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline,]
    list_display = ('name',)
admin.site.register(Recipe, RecipeAdmin)
