from django.contrib import admin
from cms.models import *

# Register your models here.
class UrlInline(admin.StackedInline):
    model = Url
    min_num = 3
    extra =0

class ProductAdmin(admin.ModelAdmin):
    inlines = [UrlInline,]

admin.site.register(Url)
admin.site.register(Product, ProductAdmin)
admin.site.register(Color_product)