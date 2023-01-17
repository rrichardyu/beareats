from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # e.g. /dashboard/
    path('', views.index, name='index'),
    # e.g. /dashboard/crossroads
    path('<str:location>/', views.dining_location, name='dining_location'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)