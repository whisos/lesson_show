from django.urls import path, include
from .views import *

urlpatterns = [
    path('', EventListView.as_view(), name= 'event_list'),
    path()
]
