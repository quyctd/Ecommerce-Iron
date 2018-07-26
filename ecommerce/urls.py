"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cms import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('home-02/', views.home_2, name='home_2'),
    path('home-03/', views.home_3, name='home_3'),
    path('product-detail/', views.product_detail, name='product_detail'),

]
