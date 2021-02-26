from django.shortcuts import render


def index(request):
    return render(request, 'orders/index.html', context={
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
