from django.db import models
from django.utils.translation import gettext as _
from django.db import IntegrityError
import random


class Category(models.Model):

    category_name = models.CharField(max_length=50,unique=True)
    category_detail = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.category_name


class Brand(models.Model):

    brand_name = models.CharField(max_length=50,unique=True)
    brand_detail = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.brand_name


class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand', blank=True, null=True)
    price = models.FloatField()


    def __str__(self):
        return self.name



"""
class Attribute(models.Model):
    container = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='attribute')
    key = models.CharField(max_length=240, db_index=True)
    value = models.CharField(max_length=240, db_index=True)

    def __str__(self):
        return self.key

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='                                                                       product_images')
    is_main = TrueUniqueBooleanField(unique_for='product')
    image_name = models.CharField(max_length=500, null=True, blank=True)
    #str(product)+'image'+str(ProductImage.objects.filter(product=product).count())

    def __str__(self):
        return self.image_name

    def save(self, *args, **kwargs):
        if not self.image_name:
            self.image_name = str(self.product)+'image'+str(ProductImage.objects.filter(product=self.product).count())
        super(ProductImage, self).save(*args, **kwargs)
        
"""
    