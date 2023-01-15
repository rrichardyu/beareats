from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import DiningLocation, MealPeriod, MenuItem, Rating

# Create your views here.
def index(request):
    return HttpResponse("You're at 'delta', the user dashboard for BearEats.")

def dining_location(request, location):
    dining_location = get_object_or_404(DiningLocation, identifier=location)
    meal_periods = dining_location.meal_periods.all()

    menu_data = {
        meal_period: [
            (
                menu_item, 
                sum([rating.rating for rating in menu_item.ratings.all()]) / len(menu_item.ratings.all()), 
                len(menu_item.ratings.all())
            ) for menu_item in meal_period.menu_items.all()
            ] for meal_period in meal_periods
        }

    context = {
        "location": dining_location,
        "menu_data": menu_data,
    }

    return render(request, "delta/dining_location.html", context)
