from rest_framework import serializers
from .models import ApiOrder

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApiOrder
#         fields = ['id', 'table_number', 'items', 'total_price', 'status']
#
#     def validate_items(self, value):
#         # Валидация списка блюд
#         if value:
#             for item in value:
#                 if 'title' not in item or 'price' not in item:
#                     raise serializers.ValidationError("Каждый элемент в items должен содержать 'title' и 'price'.")
#                 if not isinstance(item['price'], (int, str)) or int(item['price']) < 0 or item['price'].isalpha():
#                     raise serializers.ValidationError("Цена должна быть положительным числом.")
#         else:
#             raise serializers.ValidationError("Ошибка в списке блюд")
#         return value
#
#
# class OrderStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApiOrder
#         fields = ['status']
#
#
# class OrderListSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ApiOrder
#         fields = ['id', 'table_number', 'items', 'total_price', 'status']
#
# class OrderDeleteSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     class Meta:
#         model = ApiOrder
#         fields = ['id']
#
# class OrderGetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApiOrder
#         fields = ['id', 'table_number', 'items', 'total_price', 'status']

from rest_framework import serializers
from .models import ApiOrder

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiOrder
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiOrder
        fields = ['status']

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiOrder
        fields = ['id', 'table_number', 'status', 'items']