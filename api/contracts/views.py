from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from django.shortcuts import get_object_or_404

from .models import Client, Contract
from .permissions import IsSalesUserOrReadOnly
from .serializers import ClientSerializer, ClientDetailSerializer, ContractSerializer, ContractDetailSerializer

# Client list view.
class ClientListView(generics.ListCreateAPIView):
    permission_classes = [IsSalesUserOrReadOnly]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    """
   #overriding the get queryset to filter data 
    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(sales_contact=user.id)
    """
# Client Detail view.
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSalesUserOrReadOnly]
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer

# Contract list view
class ContractListView(generics.ListCreateAPIView):
    permission_classes = [IsSalesUserOrReadOnly]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

# Contract list view
class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSalesUserOrReadOnly]
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer
    lookup_field = 'id'

    def retrieve(self, request, pk=None, id=None):
        item = get_object_or_404(self.queryset, client_id=pk, id=id)
        serializer = self.get_serializer(item)
        return Response(serializer.data)

class ClientListDetailfilter(generics.ListAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^company_name', '^first_name']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

