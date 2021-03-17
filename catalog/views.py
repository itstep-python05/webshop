from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
import json


def index(request):
    return render(request, 'catalog/index.html', context={
        'title': 'Галерея товаров',
        'all_products': Product.objects.all()
    })

def create(request):
    return render(request, 'catalog/create.html', context={
        'title': 'Добавление товара'
    })

def details(request, id):
    return render(request, 'catalog/details.html', context={
        'title': 'Просмотр товара'
    })


def update(request, id):
    return render(request, 'catalog/update.html', context={
        'title': 'Редактирование товара'
    })


def delete(request, id):
    return render(request, 'catalog/delete.html', context={
        'title': 'Удаление товара'
    })


def select(request, cid):
    return render(request, 'catalog/select.html', context={
        'title': 'Выборка по категории',
        'sel_goods': Product.objects.filter(category_id=cid)
    })


def ajax_select(request):
    response = dict()
    cid = request.GET['trans_cid']
    sel_products = Product.objects.filter(category_id=cid)

    dict_products = list()
    for sp in sel_products:
        dict_products.append({
            'title': sp.title,
            'about': sp.about,
            'producer': sp.producer_id,
            'category': sp.category_id,
            'picture': str(sp.picture),
            'price': sp.price,
            'count': sp.count
        })

    json_products = json.dumps(dict_products)
    response['sel_products'] = json_products
    return JsonResponse(response)
