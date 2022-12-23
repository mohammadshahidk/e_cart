from django.shortcuts import render

from rest_framework import viewsets

from store import serializers as store_serializers
from store import models as store_models


class ProductView(viewsets.ModelViewSet):
    """
    View for Products
    """
    serializer_class = store_serializers.ProductSerializer
    queryset = store_models.Product.objects.all()


class CartItemView(viewsets.ModelViewSet):
    """
    View for cart items
    """
    serializer_class = store_serializers.CartItemSerializer
    queryset = store_models.CartItem.objects.all()


class CartView(viewsets.ModelViewSet):
    """
    View for cart
    """
    serializer_class = store_serializers.CartSerializer
    queryset = store_models.Cart.objects.all()


