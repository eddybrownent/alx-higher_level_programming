// Add a click event handler to the 'DIV' element with the ID 'red_header'
// When the 'DIV' is clicked, changes the text color of all 'HEADER' elements to red using jQuery
$('DIV#red_header').click(function () {
  $('HEADER').css('color', '#FF0000');
});
