from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from accounts import serializers as user_serializer
from accounts.models import ProjectUser


class UserView(viewsets.ModelViewSet):
    """
    View for user.
    """
    serializer_class = user_serializer.UserSerializer
    queryset = ProjectUser.objects.all()


class LoginView(generics.CreateAPIView):
    """View for login."""
    serializer_class = user_serializer.LoginSerializer




