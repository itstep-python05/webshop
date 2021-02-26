from django.shortcuts import render


def entry(request):
    return render(request, 'account/entry.html')


def logout(request):
    return render(request, 'account/logout.html')


def reg(request):
    return render(request, 'account/reg.html')
