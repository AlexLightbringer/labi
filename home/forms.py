from django import forms

from .models import Job, Order

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["name", "phone", "email", "text"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["client", "phone", "email", "order", "file_upload"]