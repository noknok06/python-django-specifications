# specification/urls.py

from django.urls import path
from .views import specification_home
from .views import StandardChangeMstCreateView, StandardChangeMstListView

urlpatterns = [
    path('', specification_home, name='specification_home'),
    path('standardchange/create/', StandardChangeMstCreateView.as_view(), name='standardchange_create'),
    path('standardchange/', StandardChangeMstListView.as_view(), name='standardchange_list'),
]
