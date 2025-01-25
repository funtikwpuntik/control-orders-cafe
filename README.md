# Cистема управления заказами в кафе
### Стек:
- Python 3.11
- Django 5.1.5
- Django Rest Framework 3.15.2
- HTML/CSS
- SQLite
### Для запуска проекта необходимо
- Скачать проект
- Создать файл .env:
    - Сгенерировать ключ можно командой *python -c 'from django.core.management.utils import get_random_secret_key; print(f\"django-insecure-{get_random_secret_key()}\")'*
    - Установить значение переменной *DJANGO_SECRET_KEY*
- Запустить виртуальное окружение
- Установить зависимости (pip install -r requirements.txt)
- Установить миграции:
  - python manage.py makemigrations 
  - python manage.py migrate
- Запустить используя команду _python manage.py runserver_


Веб-приложение на Django для управления заказами в кафе. Приложение позволяет добавлять, удалять, искать, изменять и отображать заказы. 

Каждый заказ должен содержит следующие поля:
id (уникальный идентификатор, генерируется автоматически)
table_number (номер стола)
items (список заказанных блюд с ценами) 
total_price (общая стоимость заказа, вычисляется автоматически)
status (статус заказа: “в ожидании”, “готово”, “оплачено”)



### Основные пути для веб-интерфейса:
- Главная страница */cafe/*
- Страница добавление заказа */cafe/add_order/*
- Страница со списком заказов */cafe/list_orders/*
- Страница для изменения статуса заказа */cafe/change_order/<int:pk>/*
- Страница для удаления заказа */cafe/delete_order/<int:pk>/*
- Модуль расчета выручки */cafe/revenue_report/*


### API
Путь до api: /cafe/api/v1/