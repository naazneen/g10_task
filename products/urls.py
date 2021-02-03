from django.urls import path, include
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('productsview/',ProductsView, name='productsview'),
    path('categories/', CategoryView, name='categories'),
    path('brands/', BrandView, name='brands'),
    path('productsedit/<int:id>', ProductEdit, name='productsedit'),
    path('categoryedit/<int:id>', CategoryEdit, name='categoryedit'),
    path('brandedit/<int:id>', BrandEdit, name='brandedit'),
]
