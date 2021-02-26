from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def index(request):
    return render(request, 'catalog/index.html', context={
    })

def create(request):
    return render(request, 'catalog/create.html', context={})

def details(request, id):
    return render(request, 'catalog/details.html', context={
    })


def update(request, id):
    return render(request, 'catalog/update.html', context={
    })


def delete(request, id):
    return render(request, 'catalog/delete.html', context={
    })