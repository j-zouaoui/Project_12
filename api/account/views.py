from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework import status

from .models import User, SupportContact, SalesContact

from .serializers import (
    UserSerializer, UserDetailSerializer,
    SalesContactSerializer, SalesContactDetailSerializer,
    SupportContactSerializer, SupportContactDetailSerializer

)

class UserListView(generics.ListCreateAPIView):
    """
    user class display a list of user and allow to create a new user and define if he is an admin, sales or support
    information are displayed on read only for any one.
    only admin user has the permission to create a new user and define its role
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Display a detail of an user and all updating data or delete objects
    information are displayed on read only for any one.
    only admin user has the permission to update or delete information related to a specific user
    """
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class SalesContactListView(generics.ListCreateAPIView):
    """
    Display only user with sales contact roll
    information are displayed on read only for any one.
    only admin user has the permission to create a new sales and define
    """
    permission_classes = [IsAdminUser]
    queryset = SalesContact.objects.all()
    serializer_class = SalesContactSerializer

class SalesContactDetailView(generics.RetrieveDestroyAPIView):
    """
    Display a detail of an sales user and all updating data or delete objects
    information are displayed on read only for any one.
    only admin user has the permission to update or delete information related to a specific sale user
    """
    permission_classes = [IsAdminUser]
    queryset = SalesContact.objects.all()
    serializer_class = SalesContactDetailSerializer

class SupportContactListView(generics.ListCreateAPIView):
    """
    Display only user with support contact roll
    information are displayed on read only for any one.
    only admin user has the permission to create a new sales and define
    """
    permission_classes = [IsAdminUser]
    queryset = SupportContact.objects.all()
    serializer_class = SupportContactSerializer

class SupportContactDetailView(generics.RetrieveDestroyAPIView):
    """
    Display a detail of an support user and all updating data or delete objects
    information are displayed on read only for any one.
    only admin user has the permission to update or delete information related to a specific support user
    """
    permission_classes = [IsAdminUser]
    queryset = SupportContact.objects.all()
    serializer_class = SupportContactDetailSerializer

