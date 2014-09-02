from django.db import models
from accounts.models import UserProfile


class Box(models.Model):
    name = models.CharField(max_length=100)
    
    
class BoxTab(models.Model):
    name = models.CharField(max_length=100)
    box = models.ForeignKey(Box)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    boxes = models.ManyToManyField(BoxTab)
    user = models.ForeignKey(UserProfile)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.ingredient

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    instruction = models.TextField()
    
    def __unicode__(self):
        return self.instruction
