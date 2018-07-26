from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, "about.html")
    
def blog(request):
    return render(request, "blog.html")
    
def blog_detail(request):
    return render(request, "blog-detail.html")

def contact(request):
    return render(request, "contact.html")

def home_2(request):
    return render(request, "home-02.html")
    
def home_3(request):
    return render(request, "home-03.html")


def product_detail(request):
    return render(request, "product-detail.html")