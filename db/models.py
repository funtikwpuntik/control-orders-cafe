from django.db import models


# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = [
        ('в ожидании', 'В ожидании'),
        ('готово', 'Готово'),
        ('оплачено', 'Оплачено'),
    ]

    table_number = models.IntegerField()
    items = models.JSONField(default=list)
    total_price = models.IntegerField(editable=False)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='в ожидании')

    def save(self, *args, **kwargs):

        self.total_price = sum(int(item['price']) for item in self.items)
        super().save(*args, **kwargs)