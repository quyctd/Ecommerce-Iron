from django.shortcuts import render
from cms.models import Product
# Create your views here.

def homepage(request):
    sales = Product.objects.exclude(sale_price = None)
    news = Product.objects.all()[:8]
    best_seller = Product.objects.order_by("-buy_count")
    context = {
        "sales" : sales,
        'news': news,
        "best_seller": best_seller
    }
    return render(request, "home-02.html", context = context)

def product(request):
    products = Product.objects.all()
    context = {
        "products" : products,
    }
    return render(request, 'product.html', context = context)

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    context = {
        "product": product,
    }
    return render(request, "product-detail.html", context = context)