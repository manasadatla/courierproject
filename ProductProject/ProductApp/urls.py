from django.contrib import admin
from django.urls import path,include

from ProductApp import views

urlpatterns = [
    path('display/',views.to_calculate_volume),
]
