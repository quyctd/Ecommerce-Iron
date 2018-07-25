from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    sale_price = models.IntegerField(blank = True, null = True)
    description = RichTextField()
    tags = TaggableManager()

    def __str__(self):
        return self.name

class Url(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.url)

class Category(models.Model):
    name = models.CharField(max_length = 255)
    