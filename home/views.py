from django.shortcuts import render, redirect
from .forms import JobForm, OrderForm

def home(request):
    return render(request, "home/index.html")

def job(request):
    if request.method != 'POST':
        form = JobForm()
    else:
        form = JobForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home/order_complete.html")
    context = {"form": form}
    return render(request, "home/index.html", context=context)


def contact(request):
    return render(request, "home/contact.html")


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            if 'file_upload' in request.FILES:
                order.file_upload = request.FILES["file_upload"]
                order.save()
                return redirect("home/order_complete.html")
    else:
        form = OrderForm()

    return render(request, "home/order.html", {"form": form})

def order_complete(request):
    return render(request, "home/order_complete.html")