$(function (){
  // sends get req and display
  // add handlers to send req for program detail data
  //$('.programs__program').on('click', send_get_req);

  // add handlers to delete button
  $('.delete').on('click', function (e) {
    const el = $(this).parent();
    e.preventDefault();
    $.ajax({
      type: 'DELETE',
      url: e.target.href,
      data: null,
      dataType: 'json',
      success: function (data, statusText, xhr) {el.remove();},
      error: function (xhr) {alert('error')}
    });
  });
});
