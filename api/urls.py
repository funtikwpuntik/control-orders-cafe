
from django.urls import path

from .views import OrderListCreateView, OrderStatusUpdateView, OrderListView, OrderDeleteView, OrderGetView, \
    RevenueReportView

urlpatterns = [
    path('orders/list/', OrderListView.as_view(), name='orders-list'),
    path('orders/get/<int:pk>/', OrderGetView.as_view(), name='order-get'),
    path('orders/create/', OrderListCreateView.as_view(), name='order-create'),
    path('orders/update_status/<int:pk>/', OrderStatusUpdateView.as_view(), name='order-update-status'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/revenue/', RevenueReportView.as_view(), name='orders-revenue'),
]