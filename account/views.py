from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        return render(request, 'account/sign_in.html', context={
            'title': 'Авторизация'
        })
    elif request.method == 'POST':
        # 1 Получение данных
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2 Проверка подлинности
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            data['color_x'] = 'red'
            data['mess_x'] = 'Пользователь не найден!'
            data['title'] = 'Отчет об авторизации'
            return render(request, 'account/report.html', context=data)
        else:
            login(request, user)
            return redirect('/home')


def sign_out(request):
    return render(request, 'account/sign_out.html', context={
        'title': 'Выход'
    })


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        return render(request, 'account/sign_up.html', context={
            'title': 'Регистрация'
        })
    elif request.method == 'POST':
        # 1 - Получение данных из формы
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # 2 - Каскад проверок достоверности данных (Валидация)
        if pass1_x != pass2_x:
            data['color_x'] = 'red'
            data['mess_x'] = 'Пароли не совпадают'
        elif pass1_x == '':
            # остальные проверки ...
            pass
        else:
            # Техническая проверка:
            #data['login'] = login_x
            #data['pass1'] = pass1_x
            #data['pass2'] = pass2_x
            #data['email'] = email_x

            # 3 Добавление пользователя в базу
            user = User.objects.create_user(login_x, email_x, pass1_x)

            # 4 Формирование отчета:
            data['title'] = 'Отчет о регистрации'
            if user is None:
                data['color_x'] = 'red'
                data['mess_x'] = 'В регистрации отказано!'
            else:
                user.save()
                data['color_x'] = 'green'
                data['mess_x'] = 'Регистрация успешно завершена!'

        return render(request, 'account/report.html', context=data)


def profile(request):
    return render(request, 'account/profile.html', context={
        'title': 'Профиль'
    })


def ajax_reg(request):
    response = dict()
    return JsonResponse(response)
