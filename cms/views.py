from django.shortcuts import render
from cms.models import Product
# Create your views here.

def homepage(request):
    products = Product.objects.all()
    context = {
        "products" : products,
    }
    return render(request, "home-02.html", context = context)

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def product_detail(request):
    return render(request, "product-detail.html")