# specification/urls.py

from django.urls import path
from .views import StandardChangeMstCreateView, StandardChangeMstListView, StandardChangeMstDetailView, StandardChangeMstUpdateView ,send_email_to_customer


urlpatterns = [
    path('', StandardChangeMstListView.as_view(), name='standardchange_list'),
    path('standardchange/create/', StandardChangeMstCreateView.as_view(), name='standardchange_create'),
    path('standardchange/<int:pk>/', StandardChangeMstDetailView.as_view(), name='standardchange_detail'),
    path('standardchange/<int:pk>/update/', StandardChangeMstUpdateView.as_view(), name='standardchange_update'), 
    path('standardchange/<int:item_id>/send-email/', send_email_to_customer, name='send_email'),  # URL パターンを追加する
]