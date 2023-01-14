from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.Model):
    user = models.ManyToManyField(User)
    when = models.DateTimeField(auto_now=True)
    rating = models.IntegerField()

class FoodItem(models.Model):
    uid = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=64)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

class MealPeriod(models.Model):
    period = models.CharField(max_length=18)
    date = models.DateField()
    items_offered = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

class DiningLocation(models.Model):
    location = models.CharField(max_length=18)
    meal_period = models.ForeignKey(MealPeriod, on_delete=models.CASCADE)
