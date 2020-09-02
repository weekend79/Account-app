from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    """A view that returns all the products to the products page"""
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def home_products(request):
    """A view that returns all the products to the products page"""
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

