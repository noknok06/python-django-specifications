# specification/urls.py

from django.urls import path
from .views import specification_home

urlpatterns = [
    path('', specification_home, name='specification_home'),
]
