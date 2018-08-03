from django.shortcuts import render
from cms.models import Product
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def sending_mail(request):
    name = request.GET.get('name', None)
    phone = request.GET.get('phone', None)
    mail = request.GET.get('email', None)
    message = request.GET.get('message', None)
    send_mail("Feedback Fashe - " + name, message, mail, ['quy.dc98@gmail.com',])
    data = {
        'is_taken':1
    }
    return JsonResponse(data)

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
