/**
 *  this script checkout a single item
*/
$(document).ready(function() {
  $('.checkout').on('click', function (){
    // collects user and phone data
    const email = $('input[name=email]')[0].value;
    const first_name = $('input[name=first_name]')[0].value;
    const last_name = $('input[name=last_name]')[0].value;
    const quantity = $('select[name=quantity]')[0].value;
    const phone_id = this.dataset['id'];

    // make sure email is provided
    if (!email) {
        alert('Email is needed');
        return;
    }

    // build cart structure to be sent to the server
    let cart = {};
    cart[phone_id] = parseInt(quantity);
    let data = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name
    }
    data.cart = cart;
    data = JSON.stringify(data);
    // send data to server
    $.post({
        'url': 'http://easybuy.digital/checkout',
        'contentType': 'application/json',
        data
    }).done((data, textStatus) => {
        // send browser to the new checkout page
        window.location = data.url;
    }).fail((xhr, statusCode, error) => {
        alert(JSON.parse(xhr.responseText).error);
    });
  });
});
