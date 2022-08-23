// makes a delete request to url and return the xhr object
function sendDeleteRequest(url) {
  const options = {
    type: 'DELETE',
    url,
    data: null,
    dataType: 'json'
  }
  return $.ajax(options);
}


// deletes an element if given or the parent of the cick event target
function doDelete(event, elementToDelete=''){
  const url = event.target.href;
  elementToDelete = elementToDelete || $(event.target).parent();
  const jqxhr = sendDeleteRequest(url);
  jqxhr.done(() => {$(elementToDelete).remove()}).fail(()=>{alert('refresh')});
}

// add delete effect when delete button is clicked
function registerDelete() {
  $('.delete').click((event) => {event.preventDefault(); doDelete(event);});
}

// add handler to fetch data into ajax-block__content then add handler for the new elements
function registerDataLink() {
  $('.data__item__link').click((event) => {
    event.preventDefault();
    loadInto('.ajax-block__content', event.target.href);
  });

  $('.back').click((event) => {
    event.preventDefault();
    loadInto('.ajax-block__content', event.target.href);
  });
}

function showNext() {
  $('.statement', $('.evaluation-content')).click(function (e) {
    $(this).next().toggleClass('hide')
  });
}

// register handlers for delete link and 'data__item__link'
function registerHandlers() {
  registerDelete();
  registerDataLink();
  showNext();
}


// Loads data from url into the target element
function loadInto(element, url) {
  $(element).load(url, (data, statusText, xhr) => {
    // register event handlers after load
    registerHandlers();
    
    // then show the loaded content
    $(element).parent().removeClass('hide');
  });
}

function showData(event) {
  event.preventDefault();
  // Load data into '.ajax-block__content' block
  loadInto('.ajax-block__content', event.target.href);
  
}





// hides an element when it is clicked
function hideOnClick(element) {
  $(element).click(function (e) {
    if (e.target == this) {
      $(this).addClass('hide');
    }
  });
}
