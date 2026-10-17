from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter().order_by('-category')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'category']