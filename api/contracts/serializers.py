from rest_framework import serializers
from .models import Contract, Client

from account.serializers import SalesContactSerializer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientDetailSerializer(serializers.ModelSerializer):
    sales_contact = SalesContactSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id', 'client', 'sales_contact', 'amount', "payment_due"]

class ContractDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'

