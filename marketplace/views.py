from django.shortcuts import render
from .models import Product
from .serializers import ProductListSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
# Create your views here.

class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
