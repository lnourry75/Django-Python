from django.shortcuts import render

from . import models

from myapp.models import Product

from .models import Product

def products(request):
    all_products = models.Product.objects.all()
    return render(request, 'myapp/products.html', {products : all_products})

def all_events(request):
    event_list = Product.objects.all()
    return render(request, 'myapp/event_list.html', 
        {'event_list': event_list})
