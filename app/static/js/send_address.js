/**
 * sends address details to server for creation
 */
$(document).ready(function() {
  $('.btn').on('click', () => {
    // get address data
    const customer_id = $('#customer_id').val();
    const region_id = $('#region_id').val();
    const city_id = $('#city_id').val();
    const town = $('#town').val();
    const phone_number = $('#phone_number').val();

    let data = {customer_id, region_id, city_id, town, phone_number};
    data = JSON.stringify(data)
    console.log(data);
    // send data to server
    $.post({
        "url": "http://easybuy.digital:8080/address",
        "contentType": "application/json",
        data
    }).done((data, statusText) => {
      alert('address created successfully proceed with payment');
    });
  });
});
