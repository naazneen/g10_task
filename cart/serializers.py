from rest_framework import serializers
from .models import *
from products.models import *

from products.models import Products
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import get_object_or_404


class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=500)
    cart_total = serializers.ReadOnlyField()
	
    class Meta:
        model = Cart
        fields = ('__all__')
        depth = 1

    def create(self, validated_data):
        cart_instance = Cart.objects.create(**validated_data)
        return cart_instance


class ProductsinCartSerializer(serializers.ModelSerializer):

    product = serializers.CharField(max_length=500)
    at_price = serializers.CharField(max_length=50, required=False)
    quantity = serializers.IntegerField(required=False)

    class Meta:
        model = ProductsinCart
        fields = ('__all__')
        depth = 1


    def create(self, validated_data):
        cart_instance, created = Cart.objects.get_or_create(user=self.context['request'].user)
        
        P_ID = validated_data.pop('product')
        products_instance = get_object_or_404(Products, id=P_ID )
        # if product in cart already?
        try:
            pid_in_cart = ProductsinCart.objects.get(cart=cart_instance, product=P_ID)
            #print("p", pid_in_cart)
            pid_in_cart.quantity += 1
            pid_in_cart.save()
            return pid_in_cart
        except:
            pass
        productsincart_instance = ProductsinCart.objects.create(**validated_data,cart=cart_instance, product=products_instance)
        #print(float(productsincart_instance.at_price*productsincart_instance.quantity))
        return productsincart_instance

