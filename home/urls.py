from django.urls import path
from .views import HomeView, JobView, ContactView, OrderView, OrderCompleteView
from .views import ServicesView, LabiExpoView, LabiBrandingView, LabiPrintView, LabiDesignView

app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('contact', ContactView.as_view(), name="contact"),
    path('job', JobView.as_view(), name="job"),
    path('order', OrderView.as_view(), name="order"),
    path('order_complete', OrderCompleteView.as_view(), name="order_complete"),
    path('services', ServicesView.as_view(), name="services"),
    path('labi_print', LabiExpoView.as_view(), name="labi_print"),
    path('labi_design', LabiDesignView.as_view(), name="labi_design"),
    path('labi_expo', LabiExpoView.as_view(), name="labi_expo"),
    path('labi_branding', LabiBrandingView.as_view(), name="labi_branding"),
]
