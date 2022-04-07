from rest_framework import serializers

from .models import Event
from account.serializers import SupportContactDetailSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event_date', 'client', 'event_status', "support_contact"]

class EventDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'