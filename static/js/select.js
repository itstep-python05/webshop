$(document).ready(() => {

    $('.input-checkbox input').click((event) => {
        let status = $(event.target).is(':checked');
        let cid = $(event.target).attr('id');
        console.log(`${cid} - ${status}`);

        $.ajax({
            url: '/catalog/ajax_select',
            data: `trans_cid=${cid}`,
            success: (result) => {
                console.log(result);
            }
        });
    });

});