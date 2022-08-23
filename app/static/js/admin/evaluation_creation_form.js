$(function (){
  // send delete request when ".delete" elements are clicked
  $('.delete').on('click', function (e){
    e.preventDefault();
    alert('You are deleting');

    const url = this.dataset.endpoint;

    $.ajax({
      type: 'DELETE',
      url: url,
      data: null,
      dataType: 'json',
      success: function (data, statusText, xhr){
        alert('Item Deleted successfully');
        window.location = data.url;
      }
    });
  });
});
