from django.db import models
from accounts.models import UserProfile


class Box(models.Model):
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
    name = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    recipe_yield = models.CharField(max_length=20)
    time_active = models.CharField(max_length=20)
    time_total = models.CharField(max_length=20)
    description = models.TextField()
    boxes = models.ManyToManyField(BoxTab)
    source = models.CharField(max_length=300)


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
