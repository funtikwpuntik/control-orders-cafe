from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ApiOrder
from .serializers import OrderSerializer, OrderStatusSerializer, OrderListSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с приложением по api.
    Реализованы CRUD операции
    """
    queryset = ApiOrder.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        # Используем разные сериализаторы для разных действий
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'update_status':
            return OrderStatusSerializer
        return OrderSerializer

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def revenue(self, request):
        # Фильтруем заказы со статусом "оплачено"
        paid_orders = ApiOrder.objects.filter(status='оплачено')

        # Считаем общую выручку
        total_revenue = sum(order.total_price for order in paid_orders)

        return Response({"total_revenue": total_revenue}, status=status.HTTP_200_OK)