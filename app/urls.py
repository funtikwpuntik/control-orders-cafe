from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add_order/', views.add_order, name='add_order'),
    path('list_orders/', views.list_orders, name='list_orders'),
    path('change_order/<int:pk>/', views.change_order, name='change_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('revenue_report/', views.revenue_report, name='revenue_report'),
    path('api/v1/', include('api.urls')),
]