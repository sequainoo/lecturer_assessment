/* Updates the cart element and takes the user to the
   cart detail page
*/
$(document).ready(function() {
  const cartEl = $('span.cart');
  const cartContainer = $('.cart-container');
  if (localStorage.cartTotal) {
    cartEl.text(localStorage.cartTotal);
  } else {
    cartEl.text('empty');
  }
  cartEl.css('color', 'red');

  // When cart container gets clicked send cart data to /cart on server
  // for the cart detailed page
  cartContainer.on('click', function() {
    // incase cart is not empty send its data to the server for page for cart
    if (localStorage.items && localStorage.quantities) {
      let items = localStorage.items.split(',');
      let quantities = localStorage.quantities.split(',');
      let queryString = '?';
      let index = 0;

      // builds the query string to be sent to the server
      while (index < items.length - 1) {
        queryString += items[index];
        queryString += '=';
        queryString += quantities[index];
        queryString += '&';
        index += 1;
      }
      queryString += items[index];
      queryString += '=';
      queryString += quantities[index];

      // builds the final url
      url = '/cart' + queryString;

      // directs the browser there
      window.location = url;
    } else {
      alert('Nothing in cart')
    }
  });
});