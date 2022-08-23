$(function() {
  // add click handler to the button that will gather and send all form data
  $('.submit').click(function () {
    // call the jquery() to return a query object that represents
    // all selected radio buttons of the criteria form
    const criteriaRadios = $(':checked', $('.criteria'));
    const statementRadios = $(':checked', $('.general-statement'));
    const questionsAnswers = $(':text', '.general-question');

    let labels = $('label', $('.criteria'));
    if (labels.length > criteriaRadios.length) {
      alert('Select all required');
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
});
