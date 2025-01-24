from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ApiOrder
from .serializers import OrderSerializer, OrderStatusSerializer, OrderListSerializer, OrderDeleteSerializer, \
    OrderGetSerializer


class OrderListCreateView(generics.CreateAPIView):
    queryset = ApiOrder.objects.all()
    serializer_class = OrderSerializer


class OrderStatusUpdateView(APIView):

    def patch(self, request, pk):
        try:
            order = ApiOrder.objects.get(pk=pk)
        except ApiOrder.DoesNotExist:
            return Response({"error": "Заказ не найден."}, status=status.HTTP_404_NOT_FOUND)

        order.delete()
        return Response({"message": "Заказ успешно удален."}, status=status.HTTP_204_NO_CONTENT)

class OrderListView(generics.ListAPIView):
    queryset = ApiOrder.objects.all()
    serializer_class = OrderListSerializer


class OrderDeleteView(APIView):

    def delete(self, request, pk):
        try:
            order = ApiOrder.objects.get(pk=pk)
        except ApiOrder.DoesNotExist:
            return Response({"error": "Заказ не найден."}, status=status.HTTP_404_NOT_FOUND)

        order.delete()
        return Response({"message": "Заказ успешно удален."}, status=status.HTTP_204_NO_CONTENT)

class OrderGetView(APIView):

    def get(self, request, pk):
        try:
            order = ApiOrder.objects.get(pk=pk)
        except ApiOrder.DoesNotExist:
            return Response({"error": "Заказ не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RevenueReportView(APIView):
    def get(self, request):
        # Фильтруем заказы со статусом "оплачено"
        paid_orders = ApiOrder.objects.filter(status='оплачено')

        # Считаем общую выручку
        total_revenue = sum(order.total_price for order in paid_orders)

        return Response({"total_revenue": total_revenue}, status=status.HTTP_200_OK)