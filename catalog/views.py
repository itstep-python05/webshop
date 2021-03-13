from django.shortcuts import render
from .models import Product
from .models import *
from django.core.paginator import Paginator


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