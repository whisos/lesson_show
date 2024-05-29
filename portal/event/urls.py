from django.urls import path, include
from .views import *

urlpatterns = [
    path('', EventListView.as_view(), name= 'event_list'),
    path('add/', AddCreateView.as_view(), name= 'add'),
    path('edit/', EditCreatekView.as_view(), name= 'edit'),
]
