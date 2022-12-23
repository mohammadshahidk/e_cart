from django.db import transaction
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework import exceptions

from accounts.models import ProjectUser

from store.models import Cart

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user.
    """
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        """Meta info."""
        model = ProjectUser
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address',
                  'password', 'image', 'username']

    @transaction.atomic()
    def create(self, validated_data):
        """Overriding the create methode"""
        validated_data['username'] = validated_data['email']
        user = super().create(validated_data)
        if 'password' in validated_data.keys():
            user.set_password(validated_data['password'])
            user.save()
        Cart.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer to Login."""
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        """Overriding create methode"""
        validated_data['username'] = validated_data['username']
        validated_data['password'] = validated_data['password']
        user = authenticate(
            username=validated_data['username'],
            password=validated_data['password'])
        if not user:
            raise exceptions.NotAuthenticated('Invalid Invalid email or password')

        return user


