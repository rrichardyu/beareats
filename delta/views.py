from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("You're at 'delta', the user dashboard for BearEats.")

def dining_location(request, location):
    return HttpResponse(f"You're at {location}")
