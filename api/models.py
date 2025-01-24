from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from db.models import Order

class ApiOrder(Order):

    class Meta:
        proxy = True
    def clean(self):
        super().clean()
        for item in self.items:
            if 'name' not in item or 'price' not in item:
                raise ValidationError("Каждый элемент в items должен содержать 'name' и 'price'.")
            if not isinstance(item['price'], (int, float)) or item['price'] < 0:
                raise ValidationError("Цена должна быть положительным числом.")

    def save(self, *args, **kwargs):
        # Вычисляем общую стоимость заказа
        self.total_price = sum(int(item['price']) for item in self.items)
        super().save(*args, **kwargs)