$(document).ready(function (){
    function clearCart(){
      if (localStorage.items && localStorage.quantities) {
        delete localStorage.items;
        delete localStorage.quantities;
        delete localStorage.cartTotal;
        $('.cart').text('Empty');
      }
    }
    // get cart from localStorage
function getCart(){
    if (localStorage.items && localStorage.quantities){
    let items = localStorage.items.split(',');
    let quantities = localStorage.quantities.split(',');
    let index = 0;
    let cart = {};

    while (index < items.length) {
        cart[items[index]] = parseInt(quantities[index]);
        index += 1;
    }
    console.log('---cart--- in getCart');
    console.log(cart);
    return cart;
    }
    alert('cart is empty');
}
    // checkout the cart items funtion
  $('button.cart-checkout').on('click', function (){
    // collect user data
    const email = $('input[name=email]')[0].value;
    const first_name = $('input[name=first_name]')[0].value;
    const last_name = $('input[name=last_name]')[0].value;

    // email cannot be omitted
    if (email == '') {
      alert('Email is needed');
      return;
    }
    // retrieve cart data
    cart = getCart();
    if (!cart){
      return;
    }
    // build datastructure to send to server
    let data = {
      'email': email,
      'first_name': first_name,
      'last_name': last_name
    }
    data.cart = cart;
    data = JSON.stringify(data);
    // send data to server via a post
    $.post({
        'url': 'http://easybuy.digital/checkout',
        'contentType': 'application/json',
        data
    }).done((data, textStatus) => {
        // take user to checkout page
        alert(textStatus)
        window.location = data.url;
    }).fail((xhr, statusCode, error) => {
        alert(JSON.parse(xhr.responseText).error);
    });
  });
//   clear art
$('.cart-clear').on('click', clearCart);
});