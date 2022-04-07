from django.urls import path
from .views import ClientListView, ClientDetailView, ContractListView, ContractDetailView, ClientListDetailfilter


urlpatterns = [
   path('client/', ClientListView.as_view()),
   path('client/custom_search/', ClientListDetailfilter.as_view(), name='Clientsearch'),
   path('client/<int:pk>/', ClientDetailView.as_view()),
   path('client/<int:pk>/contract/', ContractListView.as_view()),
   path('client/<int:pk>/contract/<int:id>', ContractDetailView.as_view()),
   # Contract urls
   #path('contract/', ContractListView.as_view()),
   ]
