from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
   path('client/<int:pk>/event/', EventListView.as_view()),
   path('client/<int:pk>/event/<int:id>', EventDetailView.as_view()),
   ]