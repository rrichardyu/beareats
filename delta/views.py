from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import DiningLocation, MealPeriod, MenuItem, Rating

# Create your views here.
def index(request):
    return HttpResponse("You're at 'delta', the user dashboard for BearEats.")

def dining_location(request, location):
    dining_location = get_object_or_404(DiningLocation, identifier=location)
    context = {
        "location": dining_location
    }
    return render(request, "delta/dining_location.html", context)
