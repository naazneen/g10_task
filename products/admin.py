from django.contrib import admin

from products.models import Products, Category,Brand


from django.contrib.auth import get_user_model

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Products, ProductsAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Brand, BrandAdmin)
