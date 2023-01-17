from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone

from .models import DiningLocation, MealPeriod, MenuItem, Rating
import datetime

# Create your views here.
def index(request):
    #return HttpResponse("You're at 'delta', the user dashboard for BearEats.")
    context = {
        "locations": DiningLocation.objects.all(),
    }

    return render(request, "delta/index.html", context)

def dining_location(request, location):
    if request.method == "POST":
        req_data = request.POST
        rating = req_data.get("star")
        selected_menu_item = MenuItem.objects.get(uid=req_data["menu_item_uid"])

        rating_object = Rating(menu_item=selected_menu_item, user=None, rating=int(rating), when=datetime.datetime.now(tz=timezone.utc))
        rating_object.save()

    dining_location = get_object_or_404(DiningLocation, identifier=location)
    meal_periods = dining_location.meal_periods.all()

    menu_data = {
        meal_period: [
            (
                menu_item, 
                round(sum([rating.rating for rating in menu_item.ratings.all()]) / len(menu_item.ratings.all()) if len(menu_item.ratings.all()) else 0, 2), 
                len(menu_item.ratings.all())
            ) for menu_item in meal_period.menu_items.all()
            ] for meal_period in meal_periods if meal_period.date == datetime.date.today()
        }

    context = {
        "location": dining_location,
        "menu_data": menu_data,
    }

    return render(request, "delta/dining_location.html", context)