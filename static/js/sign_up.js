function example1() {
    alert('Привет, пользователь!');
    let client = prompt('Как Вас зовут?');
    alert('Будем знакомы, ' + client + '!');
}


function example2() {
    let answer = confirm('Вы хотит посетить сайт bing.com?');
    if (answer === true) {
        window.location = 'https://www.bing.com';
    } else {
        alert('Ну не хотите, и не надо!');
    }
}


$(document).ready(() => {

    // Сценарий валидации данных, вводимых в форму регистрации:
    let r1 = false;  // результат валидации логина
    let r2 = false;   // резульата валидации поля ароль
    let r3 = false;   // результат валидации повторного вводв пароля
    let r4 = false;   // результат валидации електронной почты

    // Валидация логина:
    $('#login').blur(() => {
        let loginX = $('#login').val();
        let loginRe = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
        if (loginRe.test(loginX)) {
            // Проверка занятости логина:
            $.ajax({
                url: '/account/ajax_reg',
                data: 'login=' + loginX,
                success: (result) => {
                    if (result.message === 'занят') {
                        $('#login_err').text('Логин - занят!!!');
                        r1 = false;
                    } else {
                        r1 = true;
                    }
                }
            });
        } else {
            $('#login_err').text('Длина логина должна быть - от 6 до 16 символов: буквы, цифры и тире, _');
        }
    });

    // Валидация 1 пароля:
    $('#pass1').blur(() => {
        let pass1X = $('#pass1').val();
        let pass1Re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-])[a-zA-Z0-9_\-]{8,}$/;
        if (pass1Re.test(pass1X)) {
            r2 = true;
            $('#pass1_err').text('');
        } else {
            r2 = false;
            $('#pass1_err').text('Пароль должен иметь не менее 8ми значений (Допускаются большин, маленькие буквы и цифры)');
        }
    });

    // Валидация 2 пароля:
    $('#pass2').blur(() => {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();
        if (pass1X === pass2X) {
            r3 = true;
            $('#pass2_err').text('');
        } else {
            r3 = false;
            $('#pass2_err').text('Пароли не совпадают');
        }
    });

    // Валидация email:
    $('#email').blur(() => {
        let emailX = $('#email').val();
        let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailRe.test(emailX)) {
            r4 = true;
            $('#email_err').text('');
        } else {
            r4 = false;
            $('#email_err').text('Стандартная почта: username@host.domain');
        }
    });

    // Итоговая проверка результатов валидации и триггер канала Submit:
    $('#submit').click(() => {
        if (r1 === true && r2 === true && r3 === true && r4 === true) {
            $('#form-1').attr('onsubmit', 'return true');
        } else {
            $('#form-1').attr('onsubmit', 'return false');
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована!');
        }
    });

    // обработка сброса сообщений об ошибках:
    $('#login').focus(() => {
        $('#login_err').text('');
    });

    $('#pass1').focus(() => {
        $('#pass1_err').text('');
    });

    $('#pass2').focus(() => {
        $('#pass2_err').text('');
    });

    $('#email').focus(() => {
        $('#email_err').text('');
    });

});