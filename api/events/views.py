from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from .models import Event
from .permissions import IsSupportUserOrReadOnly
from .serializers import EventSerializer, EventDetailSerializer


# Create your views here.
class EventListView(generics.ListCreateAPIView):
    permission_classes = [IsSupportUserOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Contract list view
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSupportUserOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = 'id'

    def retrieve(self, request, pk=None, id=None):
        item = get_object_or_404(self.queryset, client_id=pk, id=id)
        serializer = self.get_serializer(item)
        return Response(serializer.data)
