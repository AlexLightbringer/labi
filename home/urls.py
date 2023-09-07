from django.contrib import admin
from django.urls import path
from .views import home, contact

app_name = "home"

urlpatterns = [
    path('', home, name="index"),
    path('contact', contact, name="contact"),
]