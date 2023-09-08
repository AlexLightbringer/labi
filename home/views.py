from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

def home(request):
    return render(request, "home/index.html")

def job(request):
    if request.method != 'POST':
        form = JobForm()
    else:
        form = JobForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "home/index.html", context=context)


def contact(request):
    return render(request, "home/contact.html")
