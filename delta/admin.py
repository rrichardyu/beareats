from django.contrib import admin

# Register your models here.
from .models import DiningLocation, MealPeriod, MenuItem, Rating

admin.site.register(DiningLocation)
admin.site.register(MealPeriod)
admin.site.register(MenuItem)
admin.site.register(Rating)