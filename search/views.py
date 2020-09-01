from django.shortcuts import render
from products.models import Product


# Create your views here.
def do_search(request):
    """A view that renders the search view"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})