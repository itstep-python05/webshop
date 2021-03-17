from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Order


def index(request):
    return render(request, 'orders/index.html', context={
        'title': 'Список заказов',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def confirm(request):
    return render(request, 'orders/confirm.html', context={
        'title': 'Подтверждение заказа',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def create(request):
    return render(request, 'orders/create.html', context={
    })


def update(request, id):
    return render(request, 'orders/update.html', context={
    })


def delete(request, id):
    return render(request, 'orders/delete.html', context={
    })


def email(request):
    return render(request, 'orders/email.html', context={
        'title': 'Почтовые уведомления'
    })


def ajax_basket(request):
    # 1 - Извлекаем параметры заказаиз AJAX-запроса:
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')

    # 2 - Создаем новый заказ и сохраняем его в базе данных:
    Order.objects.create(
        title=f'Order-{pid}/{uid}',
        amount=float(price),
        status='Ожидание подтверждения',
        product_id=pid,
        user_id=uid,
    )

    # 3 - Извлекаем список заказов данного пользователя:
    user_orders = Order.objects.filter(user_id=uid)

    # 4 - Вычисляем общую стоимость всех покупок данного пользователя:
    s = 0
    for order in user_orders:
        s += order.amount

    # 5 - Записываем в ответ общую стоимость и количество товаров:
    response['amount'] = s
    response['count'] = len(user_orders)

    # 6 - Отправляем ответ в JS:
    return JsonResponse(response)


def ajax_basket_display(request):
    # 0 - Создаем пустой словарь для сборки ответа на AJAX-запроса:
    response = dict()
    # 1 - Извлекаем ID пользователя из AJAX-запроса:
    uid = request.GET['uid']

    # 3 - Извлекаем список заказов данного пользователя:
    user_orders = Order.objects.filter(user_id=uid)

    # 4 - Вычисляем общую стоимость всех покупок данного пользователя:
    s = 0
    for order in user_orders:
        s += order.amount

    # 5 - Записываем в ответ общую стоимость и количество товаров:
    response['amount'] = s
    response['count'] = len(user_orders)
    return JsonResponse(response)
