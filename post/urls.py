import imp
from re import I
from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name="index")
]