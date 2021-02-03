from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, generics
import requests
from rest_framework.decorators import api_view, permission_classes
from .models import Products
from .serializers import *
import sys


@api_view(('POST', 'GET',))
@permission_classes([IsAdminUser])
def ProductsView(request):
    try:
        if request.method == 'POST':
            serializer = ProductsFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == 'GET':
            lb = Products.objects.all()
            serializer = ProductsFormSerializer(lb, many=True)
            this_data = serializer.data
            return Response(this_data, status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method
            return Response({'detail': context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(('POST', 'GET',))
@permission_classes([IsAdminUser])
def CategoryView(request):
    try:
        if request.method == 'POST':
            serializer = CategoryFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == "GET":
            c = Category.objects.all()
            serializer = CategoryFormSerializer(c, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method
            return Response({'detail': context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(('POST', 'GET',))
@permission_classes([IsAdminUser])
def BrandView(request):
    try:
        if request.method == 'POST':
            serializer = BrandFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == "GET":
            c = Brand.objects.all()
            serializer =BrandFormSerializer(c, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method
            return Response({'detail': context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(('PATCH', 'GET','DELETE'))
@permission_classes([IsAdminUser])
def ProductEdit(request, id):
    try:
        if request.method == 'GET':
            p = get_object_or_404(Products, id=id)
            this_data = ProductsFormSerializer(p).data
            if this_data.get('attributes') :
                attribs = {}
                for k in this_data['attributes']:
                    attribs[k['key']] = k['value']
                this_data['attributes'] = attribs

            context = {}
            context['data'] = this_data
            return Response(context, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            p = get_object_or_404(Products, id=id)
            serializer = ProductsFormSerializer(p, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == 'DELETE':
            p = get_object_or_404(Products, id=id)
            p.delete()
            return Response("Product Deleted", status=status.HTTP_200_OK)

        else:
            context = {}
            context['method'] = request.method

            return Response({'detail':context}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(('PATCH', 'GET','DELETE'))
@permission_classes([IsAdminUser])
def CategoryEdit(request, id):
    try:
        if request.method == 'GET':
            c = get_object_or_404(Category, id=id)
            return Response(CategoryFormSerializer(c).data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            c = get_object_or_404(Category, id=id)
            serializer = CategoryFormSerializer(c, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == 'DELETE':
            c = get_object_or_404(Category, id=id)
            c.delete()
            return Response("Category Deleted", status=status.HTTP_200_OK)
        else:
            context = {}
            context['method'] = request.method
            return Response({'detail':context}, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(('PATCH', 'GET','DELETE'))
@permission_classes([IsAdminUser])
def BrandEdit(request, id):
    try:
        if request.method == 'GET':
            c = get_object_or_404(Category, id=id)
            return Response(BrandFormSerializer(c).data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            c = get_object_or_404(Category, id=id)
            serializer = BrandFormSerializer(c, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)

        elif request.method == 'DELETE':
            c = get_object_or_404(Brand, id=id)
            c.delete()
            return Response("Brand Deleted", status=status.HTTP_200_OK)
        else:
            context = {}
            context['method'] = request.method
            return Response({'detail':context}, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        context = {}
        context['details'] = str(sys.exc_info())
        return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




