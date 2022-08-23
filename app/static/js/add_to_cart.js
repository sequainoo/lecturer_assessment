$(document).ready(function (){
  /* Get localstorage and update it with the productId and quantity pair
    localstorage.items store the productids and localstorage.quantities
    stores the corresponding quantities
  */
  function addToCart(productId, quantity) {
    // checks values to make sure they are right
    if (!quantity || !productId || !parseInt(quantity)) {
      throw new Error('Your Values are empty');
    }
    if (typeof(productId) !== 'string') {
      throw new Error('Bad type for product id');
    }
    let items = [];
    let quantities = []

    // if localstorage has cart data already update it with the new data
    if (localStorage.items && localStorage.quantities) {
        items = localStorage.items.split(',');
        quantities = localStorage.quantities.split(',');

        if (items.includes(productId)) {
            const index = items.indexOf(productId);
            quantities[index] = parseInt(quantities[index]) + quantity;
        } else {
            items.push(productId);
            quantities.push(parseInt(quantity));
        }
        localStorage.cartTotal = parseInt(localStorage.cartTotal) + quantity;
    } else {
        items = [productId]
        quantities = [quantity];
        localStorage.cartTotal = quantity;
    }
    localStorage.items = items;
    localStorage.quantities = quantities;
  }

  $('.add-to-cart').on('click', function() {
    const productId = this.dataset['id'];
    const quantity = parseInt($('select[name=quantity]').val());

    if (!quantity) {
      alert('Quantity Looks funny, Checkout other items');
      return;
    }

    addToCart(productId, quantity);
    $('span.cart').text(localStorage.cartTotal);
    $('span.cart').css('color', 'red');
  });
});