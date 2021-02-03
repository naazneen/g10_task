from django.urls import path, include
from rest_framework.authtoken import views
from .views import *


urlpatterns = [

    path('products-in-cart/', ProductsinCartView, name='products-in-cart'),
    path('mycart/', MyCartView, name='mycart'),
    path('update-cart-product/<str:pid>', UpdateCartProduct, name='update-cart-product'),

]