import json

from django import forms

from db.models import Order

class OrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = [
            'table_number',
            'items',
        ]
        labels = {
            'table_number': 'Номер стола',
            'items': 'Список блюд',
        }

        widgets = {
            'table_number': forms.TextInput(attrs={
                'placeholder': 'Введите номер стола',  # Текст внутри поля
                'class': 'form-control',
            }),
            'items': forms.TextInput(attrs={
                'placeholder': 'Введите список блюд через запятую.',  # Текст внутри поля
                'class': 'form-control',
            }),
            # 'user': forms.HiddenInput(),
            # 'video_format': forms.HiddenInput()
        }
        #
    # def __init__(self, *args, **kwargs):
    #     print(kwargs.get('items'))
    #     self.total_price = sum([float(item['price']) for item in kwargs.get('items')])
    #     self.status = 'в ожидании'
    #     super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_price = sum([float(item['price']) for item in instance.items])
        instance.status = 'в ожидании'
        if commit:
            instance.save()
        return instance




class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

        labels = {
            'status': 'Новый статус',
        }