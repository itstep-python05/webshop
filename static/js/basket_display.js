$(document).ready(() => {

    const user_id = $('#user_id').val();

    $.ajax({
        url: '/orders/ajax_basket_display',
        data: `uid=${user_id}`,
        success: (result) => {
            // Отображение изменений в иконке корзины:
            let count = result.count;
            let amount = result.amount;
            $('#count').text(`Количество товаров: ${count} шт`);
            $('#amount').text(`Общая стоимость: ${amount} грн`);
            $('#_count').text(count);
        }
    });

});