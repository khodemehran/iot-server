from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.home, name = 'home'),
    path('add_data/',views.add_data, name = 'add_data'),

    
]