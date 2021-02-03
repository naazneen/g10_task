
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, generics
import requests
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
import sys
from datetime import datetime,timedelta

# Create your views here.


@api_view(('POST', 'GET',))
@permission_classes([IsAuthenticated])
def ProductsinCartView(request):
    try:
        if request.method == 'POST':
            c, created = Cart.objects.get_or_create(user=request.user)
            serializer = ProductsinCartSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)
        
        elif request.method == "GET":
            c, created = Cart.objects.get_or_create(user=request.user)
            p = ProductsinCart.objects.filter(cart=Cart.objects.get(user=request.user))
            serializer = ProductsinCartSerializer(p, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method
            return Response({'detail': context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        context = {}
        print(e)
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(('GET','POST',))
@permission_classes([IsAuthenticated])
def MyCartView(request):
    try:
        
        if request.method == "GET":
            c, created = Cart.objects.get_or_create(user=request.user)
            c = Cart.objects.get(user=request.user)
            serializer = CartSerializer(c,context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            c, created = Cart.objects.get_or_create(user=request.user)
            serializer = CartSerializer(c,context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method
            return Response({'detail': context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        context = {}
        print(e)
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('PATCH', 'GET','DELETE',))
@permission_classes([IsAuthenticated])
def UpdateCartProduct(request,pid):
    try:
        if request.method == 'GET':
            p_in_c = get_object_or_404(ProductsinCart, product_fromvendor=pid)
            this_data = ProductsinCartSerializer(p_in_c,context={'request': request}).data
            return Response(this_data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            p_in_c = get_object_or_404(ProductsinCart, product_fromvendor=pid)
            serializer = ProductsinCartSerializer(p_in_c,context={'request': request}, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == 'DELETE':
            p_in_c = get_object_or_404(ProductsinCart, product_fromvendor=pid)
            p_in_c.delete()
            return Response("Product Removed from Cart", status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method

            return Response({'detail':context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        