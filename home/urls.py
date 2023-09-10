from django.urls import path
from .views import home, contact, job, order, order_complete


app_name = "home"

urlpatterns = [
    path('', home, name="index"),
    path('contact', contact, name="contact"),
    path('job', job, name="job"),
    path('order', order, name="order"),
    path('order_complete/', order_complete, name='order_complete'),  # URL для страницы "complete.html"
]
