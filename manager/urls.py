# manager/urls.py

from django.urls import path
from .views import manager_home

urlpatterns = [
    path('', manager_home, name='manager_home'),
]
