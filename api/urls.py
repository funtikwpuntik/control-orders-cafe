
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)
urlpatterns = [
    # path('orders/list/', OrderListView.as_view(), name='orders-list'),
    # path('orders/get/<int:pk>/', OrderGetView.as_view(), name='order-get'),
    # path('orders/create/', OrderListCreateView.as_view(), name='order-create'),
    # path('orders/update_status/<int:pk>/', OrderStatusUpdateView.as_view(), name='order-update-status'),
    # path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
    # path('orders/revenue/', RevenueReportView.as_view(), name='orders-revenue'),
]

urlpatterns.extend(router.urls)