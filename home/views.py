from django.views.generic import CreateView, TemplateView
from .models import Job, Order
from .forms import JobForm, OrderForm
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "home/index.html"


class JobView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "home/index.html"
    success_url = "order_complete"


class ContactView(TemplateView):
    template_name = "home/contact.html"


class OrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "home/order.html"
    success_url = "order_complete"


class OrderCompleteView(TemplateView):
    template_name = "home/order_complete.html"


class ServicesView(TemplateView):
    template_name = "home/services.html"


class LabiPrintView(TemplateView):
    template_name = "home/print.html"


class LabiExpoView(TemplateView):
    template_name = "home/expo.html"


class LabiDesignView(TemplateView):
    template_name = "home/design.html"


class LabiBrandingView(TemplateView):
    template_name = "home/branding.html"


def page_not_found_view(request, exception):
    return render(request, "home/errors/404.html", status=404)
