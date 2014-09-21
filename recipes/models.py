from django.db import models
from accounts.models import UserProfile
from utils import pkgen


class Box(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile)

    class Meta:
        verbose_name_plural = "boxes"

    def __unicode__(self):
        return self.name
    
    
class BoxTab(models.Model):
    name = models.CharField(max_length=100)
    box = models.ForeignKey(Box)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pkgen)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    recipe_yield = models.CharField(max_length=50, blank=True)
    time_active = models.CharField(max_length=50, blank=True)
    time_total = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    source = models.CharField(max_length=300, blank=True)
    #privacy = models.CharField(max_length=10)
    boxes = models.ManyToManyField(BoxTab)


    def __unicode__(self):
        return self.name


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
