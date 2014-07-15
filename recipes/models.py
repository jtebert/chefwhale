from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.CharField(max_length=100)

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    instruction = models.TextField()
