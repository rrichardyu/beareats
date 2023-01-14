from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiningLocation(models.Model):
    location = models.CharField(max_length=18)
    
class MealPeriod(models.Model):
    location = models.ForeignKey(DiningLocation, on_delete=models.CASCADE, null=True, blank=False)
    period = models.CharField(max_length=18)
    date = models.DateField()

class MenuItem(models.Model):
    meal_period = models.ForeignKey(MealPeriod, on_delete=models.CASCADE, null=True, blank=False)
    uid = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=64)

class Rating(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    rating = models.IntegerField()
    when = models.DateTimeField()

# TODO: write string representations of models