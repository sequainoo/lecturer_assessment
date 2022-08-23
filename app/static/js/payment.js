$(document).ready(function () {
  $('a.pay').on('click', function () {
    let order_id = $('#order_id').val();
    let public_key = $('#public_key').val();
    let tx_ref = $('#tx_ref').val();
    let amount = $('#amount').val();
    let customer_id = $('#customer_id').val();
    let customer_email = $('#customer_email').val();
    let customer_name = $('#customer_name').val();
    let customer_phone_number = $('#customer_phone_number').val();

    makePayment();

    function makePayment() {
      // customer phone is from address so if is not there address is not there
      if (! customer_phone_number) {
        alert('You Do not have an address!');
        return
      }
      // call this class from flutterwave api library with payment details as obj
      const modal = FlutterwaveCheckout({
        public_key,
        tx_ref,
        amount,
        currency: "GHS",
        payment_options: "card, mobilemoneyghana",
        callback: function(paymentResponse) {
          // verify transaction on server
          verifyTransaction(paymentResponse);
        },
        onclose: function(incomplete) {
          if (incomplete) {
            $('#fail').css('display', 'flex');
        }
        },
        meta: {
          consumer_id: customer_id,
        },
        customer: {
          email: customer_email,
          phone_number: customer_phone_number,
          name: customer_name,
        },
        customizations: {
          title: "EasyBuy Store",
          description: "Payment for Phone"
        },
      });

      // verifies transaction ddetails
    function verifyTransaction(paymentResponse) {
      payload = {};
      payload.status = paymentResponse.status;
      payload.tx_ref = paymentResponse.tx_ref;
      payload.transaction_id = paymentResponse.transaction_id;
      payload.order_id = order_id;

      $.post({
        url: "http://easybuy.digital/payment",
        contentType: "application/json",
        data: JSON.stringify(payload)
      }).done((data, textResponse) => {
        if (data.status === 'error') {
            modal.close();
            $('#fail').css('display', 'flex');
            $('.payment-form').css('display', 'none');
        } else if (data.status === 'success') {
            modal.close();
            $('.payment-form').css('display', 'none');
            $('#success').css('display', 'flex');
            setTimeout(() => {
              window.location = 'http://easybuy.digital/phones';
            }, 500);
        }
      });
    }
    }
  });
});