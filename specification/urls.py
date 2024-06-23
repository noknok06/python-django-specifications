# specification/urls.py

from . import views
from django.urls import path
from .views import StandardChangeMstCreateView, StandardChangeMstListView, StandardChangeMstDetailView, StandardChangeMstUpdateView ,StandardChangeSendHistoryListView, send_email_to_customer, get_item_name


urlpatterns = [
    path('standardchange/', StandardChangeMstListView.as_view(), name='standardchange_list'),
    path('standardchange/create/', StandardChangeMstCreateView.as_view(), name='standardchange_create'),
    path('standardchange/<int:pk>/', StandardChangeMstDetailView.as_view(), name='standardchange_detail'),
    path('standardchange/<int:pk>/update/', StandardChangeMstUpdateView.as_view(), name='standardchange_update'), 
    path('standardchange/<int:item_id>/send-email/', send_email_to_customer, name='send_email'),  # URL パターンを追加する
    path('check_item_id/', views.check_item_id, name='check_item_id'),
    path('standardchange/<int:pk>/delete/', views.standardchange_delete, name='standardchange_delete'),
    path('standardchange/<int:item_id>/history', StandardChangeSendHistoryListView.as_view(), name='standardchange_send_history'),
    path('get_item_name/', get_item_name, name='get_item_name'),
]