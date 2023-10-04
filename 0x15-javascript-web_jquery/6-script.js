// Add a click event handler to the 'DIV' element with the ID 'update_header'
// When the 'DIV' is clicked, change the text content of all 'HEADER' elements to 'New Header!!!' using jQuery
$('DIV#update_header').click(function () {
  $('HEADER').text('New Header!!!');
});
