from django.urls import path
from .views import (
    UserListView, UserDetailView,
    SalesContactListView, SalesContactDetailView,
    SupportContactListView, SupportContactDetailView

)

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    #sales urls
    path('user/sales/', SalesContactListView.as_view()),
    path('user/sales/<int:pk>/', SalesContactDetailView.as_view()),
    #support urls
    path('user/support/', SupportContactListView.as_view()),
    path('user/support/<int:pk>/', SupportContactDetailView.as_view()),
]
