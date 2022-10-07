$(function() {
  // add click handler to the button that will gather and send all form data
  $('.submit').click(function () {
    // call the jquery() to return a query object that represents
    // all selected radio buttons of the criteria form
    const criteriaRadios = $(':checked', $('.criteria'));
    const statementRadios = $(':checked', $('.general-statement'));
    const questionsAnswers = $(':text', '.general-question');

    const errorParagraph = $('<p class="error-paragraph">You cannot submit</p>');
    let labels = $('label', $('.criteria'));
    if (labels.length > criteriaRadios.length) {
      const left = $(this).offset().left + $(this).outerWidth();
      const top = $(this).offset().top;
      errorParagraph[0].style.left = left + 10 + 'px';
      errorParagraph[0].style.top = (top - 40) + 'px';
      $(this).before(errorParagraph);
      setTimeout(()=> {errorParagraph.remove()}, 1500);
      return;
    }
    
    labels = $('label', $('.general-statement'));
    if (labels.length > statementRadios) {
      alert('Select all required');
      return;
    }
    // Take datasets of the criteria form selected radios and add them to a list
    const criteriaDatasets = [];
    criteriaRadios.each(function () {criteriaDatasets.push(this.dataset)});

    const statementsDatasets = [];
    statementRadios.each(function (){statementsDatasets.push(this.dataset)});
    
    const answersDatasets = [];
    questionsAnswers.each(function (){
      this.dataset.answer = $(this).val();
      answersDatasets.push(this.dataset);
    });
  
    let body = JSON.stringify({criteriaDatasets, statementsDatasets, answersDatasets});
    console.log(body)
    const url = '/evaluate/' + $('.course-id-holder').val();
    $.ajax({
      type: 'POST',
      url: url,
      data: body,
      dataType: 'json',
      contentType: 'application/json',
      success: (data, statusText, xhr) => {window.location=data.url},
      error: (xhr) => {this.disabled='';},
    });
    this.disabled = 'disabled';
  });

  // Control how much data ccomes on the page
  // Only few questions are displayed and the rest are hidden from view
  const hidden_blobs =  getHiddenBlobs();
  let pointer = 0;
  let parentForm = hidden_blobs[pointer].parent();
  
  // show the first
  parentForm.css('display','block');
  hidden_blobs[pointer].removeClass('hide');

  // when the next button is clicked hide the currently displayed data
  // and show the next
  $('.next').click(function() {
    if (pointer < hidden_blobs.length - 1) {
      parentForm.css('display', 'none');
      hidden_blobs[pointer].addClass('hide');
      pointer ++;
      parentForm = hidden_blobs[pointer].parent();
      parentForm.css('display', 'block');    
      hidden_blobs[pointer].removeClass('hide');
    }    
  });

  // move back when prev button is pressed
  $('.prev').click(function() {
    if (pointer > 0) {
      parentForm.css('display', 'none');
      hidden_blobs[pointer].addClass('hide');
      pointer --;
      parentForm = hidden_blobs[pointer].parent();
      parentForm.css('display', 'block');    
      hidden_blobs[pointer].removeClass('hide');
    }
  });
   
});
