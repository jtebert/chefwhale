from django.contrib import admin
from recipes.models import *

class IngredientInline(admin.TabularInline):
    model = Ingredient


class InstructionInline(admin.TabularInline):
    model = Instruction


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline, ]
    list_display = ('name',)


admin.site.register(Recipe, RecipeAdmin)


class BoxTabInline(admin.TabularInline):
    model = BoxTab


class BoxAdmin(admin.ModelAdmin):
    inlines = [BoxTabInline, ]


admin.site.register(Box, BoxAdmin)