from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from app.forms import OrderForm, OrderStatusForm
import json

from db.models import Order

from django.db.models import Sum, Q


def revenue_report(request):
    total_revenue = Order.objects.filter(status='оплачено').aggregate(Sum('total_price'))['total_price__sum']
    return render(request, 'revenue_report.html', {'total_revenue': total_revenue})
def index(request):
    return render(request, 'index.html')


def add_order(request):
    if request.POST:
        post_data = request.POST.copy()
        post_data['items'] = request.POST.getlist('items')
        post_data['table_number'] = request.POST.get('table_number')
        json_items = []
        for item in post_data['items']:
            item = item.split()
            title, price = ' '.join(item[:-1]), item[-1]
            json_items.append(
                {
                    'title': title,
                    'price': price,
                }
            )

        post_data['items'] = json.dumps(json_items, ensure_ascii=False)
        form = OrderForm(post_data)
        if form.is_valid():
            form.save()
    form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def list_orders(request):
    query = request.GET.get('q')  # Получаем поисковый запрос
    if query:
        query = query.lower()
        # Ищем заказы по номеру стола или статусу
        orders = Order.objects.filter(
            Q(table_number__icontains=query) | Q(status__icontains=query)
        )
    else:
        # Если запрос пустой, показываем все заказы
        orders = Order.objects.all()
    return render(request, 'list_orders.html', {'orders': orders})

def change_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('list_orders')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'change_order.html', {'form': form, 'order': order})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('list_orders')
    return render(request, 'delete_order.html', {'order': order})
