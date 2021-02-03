from rest_framework import serializers
from .models import *


class CategoryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        depth = 1

    category_name = serializers.CharField()
    category_detail = serializers.CharField(required=False)

    def create(self, validated_data):
        category_instance = Category.objects.create(**validated_data)
        return category_instance

class BrandFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        depth = 1

    brand_name = serializers.CharField()
    brand_detail = serializers.CharField(required=False)

    def create(self, validated_data):
        brand_instance = Brand.objects.create(**validated_data)
        return brand_instance



class ProductsFormSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=1000)
    category = serializers.CharField(required=False)
    brand = serializers.CharField(required=False)

    class Meta:
        model = Products
        fields = ('__all__')
        depth = 1

    def create(self, validated_data):
        #subcat_name = validated_data.pop("subcategory")
        if validated_data.get("category") and validated_data.get("brand"):
            cat_name = validated_data.pop("category")
            brand_name = validated_data.pop("brand")
            cat_inst, created = Category.objects.get_or_create(category_name=cat_name)
            brd_inst, created = Brand.objects.get_or_create(brand_name=brand_name)
            products_instance = Products.objects.create(**validated_data,category=cat_inst, brand=brd_inst)

        elif validated_data.get("category"):
            cat_name = validated_data.pop("category")
            cat_inst, created = Category.objects.get_or_create(category_name=cat_name)
            products_instance = Products.objects.create(**validated_data,category=cat_inst)


        elif validated_data.get("brand"):
            brand_name = validated_data.pop("brand")
            brd_inst, created = Brand.objects.get_or_create(brand_name=brand_name)
            products_instance = Products.objects.create(**validated_data, brand=brd_inst)
        
        else:
            products_instance = Products.objects.create(**validated_data)


        return products_instance
    
    