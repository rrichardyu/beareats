from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiningLocation(models.Model):
    location = models.CharField(max_length=18)

    def __str__(self):
        return f"{self.location}"

class MealPeriod(models.Model):
    location = models.ForeignKey(DiningLocation, on_delete=models.CASCADE, null=True, blank=False)
    period = models.CharField(max_length=18)
    date = models.DateField()

    def __str__(self):
        return f"{self.period} at {self.location.location} on {str(self.date)}"

class MenuItem(models.Model):
    meal_period = models.ForeignKey(MealPeriod, on_delete=models.CASCADE, null=True, blank=False)
    uid = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} ({self.category}) during {self.meal_period.period} at {self.meal_period.location.location} (UID: {self.uid})"

class Rating(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    rating = models.IntegerField()
    when = models.DateTimeField()

    def __str__(self):
        return f"{self.menu_item.name} rated {self.rating} by {self.user.username} on {str(self.when)}"