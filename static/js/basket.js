$(document).ready(() => {

    $('.add-to-cart-btn').click((event) =>{
        // 1 - Определение параметров заказа:
        const user_id = $('#user_id').val();
        if (user_id == 'None') {
            alert('Для использования корзины вы должны авторизоваться!');
            window.location = '/account/sign_in';
        } else {
            let uid = user_id;
            let pid = $(event.target).prev().val();
            let price = $(event.target).parent().prev().find('h4').text()

            // 2 - Отпрака AJAX запроса на добавление заказа в БД:
            $.ajax({
                url: '/orders/ajax_basket',
                data: `uid=${uid}&pid=${pid}&price=${price}`,
                success: (result) => {
                    // Отображение изминеий в иконке корзины:
                    alert('Товар успешно добавлен в корзину!');
                    let count = result.count;
                    let amount = result.amount;
                    $('#count').text(`Количество товаров: ${count} шт`);
                    $('#amount').text(`Общая стоимость: ${amount} грн`);
                    $('#_count').text(count);
                }
            });
        }

    });

});