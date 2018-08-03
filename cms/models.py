from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from datetime import datetime, timedelta, timezone

# Create your models here.

class Color_product(models.Model):
    color = models.CharField(max_length = 255)

    def __str__(self):
        return self.color

class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    sale_price = models.IntegerField(blank = True, null = True)
    sort_info = models.TextField()
    description = RichTextField(blank = True, null = True)
    addtional_info = models.TextField(blank= True, null = True)
    buy_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(default = datetime.now())
    colors = models.ManyToManyField(Color_product)
    tags = TaggableManager()

    def is_new(self):
        end = self.created_date + timedelta(days=7)
        now = datetime.now(timezone.utc)
        if now < end:
            return True
        return False

    def __str__(self):
        return self.name
    

class Url(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.url)

class Category(models.Model):
    name = models.CharField(max_length = 255)
    