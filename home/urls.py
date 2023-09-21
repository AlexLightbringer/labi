from django.urls import path
from .views import home, contact, job, order, order_complete, services, labi_print, labi_design, labi_expo, labi_branding


app_name = "home"

urlpatterns = [
    path('', home, name="index"),
    path('contact', contact, name="contact"),
    path('job', job, name="job"),
    path('order', order, name="order"),
    path('order_complete', order_complete, name="order_complete"),
    path('services', services, name="services"),
    path('labi_print', labi_print, name="labi_print"),
    path('labi_design', labi_design, name="labi_design"),
    path('labi_expo', labi_expo, name="labi_expo"),
    path('labi_branding', labi_branding, name="labi_branding"),
]
