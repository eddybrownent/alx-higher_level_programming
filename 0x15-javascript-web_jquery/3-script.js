// Add a click event handler to the 'DIV' element with the ID 'red_header'
// When the 'DIV' is clicked, add the 'red' class to all 'HEADER' elements using jQuery
$('DIV#red_header').click(function () {
  $('HEADER').addClass('red');
});
