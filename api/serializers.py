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