from django.urls import path
from . import views

urlpatterns = [
    # e.g. /dashboard/
    path('', views.index, name='index'),
    # e.g. /dashboard/crossroads
    path('<str:location>/', views.dining_location, name='dining_location')
]