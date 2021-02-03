from django.db import models
from products.models import Products
from django.conf import settings


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    @property
    def cart_total(self):
        total = 0.0
        for p in self.products_incart.all():
            total += float(float(p.at_price)*p.quantity)
        
        return total


    


class ProductsinCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products_incart')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
    at_price = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        super(ProductsinCart, self).save(*args, **kwargs)
        self.at_price = self.product.price
        super(ProductsinCart, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
