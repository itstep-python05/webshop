from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', context={
        'title': 'Главная'
    })


def about(request):
    return render(request, 'home/about.html', context={
        'title': 'Про сайт'
    })


def contacts(request):
    return render(request, 'home/contacts.html', context={
        'title': 'Контакты'
    })
