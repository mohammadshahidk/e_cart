from rest_framework import serializers

from store import models as store_models


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Products
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        """Meta info."""
        model = store_models.Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Cart
    """
    id = serializers.IntegerField(read_only=True)
    sub_total = serializers.CharField(read_only=True)

    class Meta:
        """Meta info"""
        model = store_models.CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer to Cart
    """
    id = serializers.CharField(read_only=True)
    grand_total = serializers.FloatField(read_only=True)

    class Meta:
        """Meta info"""
        model = store_models.Cart
        fields = '__all__'





