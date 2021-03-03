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
    let r1 = false;
    let r2 = true;
    let r3 = true;
    let r4 = true;

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

    $('#submit').click(() => {
        if (r1 === true && r2 === true && r3 === true && r4 === true) {
            $('#form-1').attr('onsubmit', 'return true');
        } else {
            $('#form-1').attr('onsubmit', 'return false');
            alert('Форма содержит некорректные данные! \nОтправка данных заблокирована!');
        }
    });

   $('#login').focus(() => {
        $('#login_err').text('');
    });

});