// Add a click event handler to the 'DIV' element with the ID 'toggle_header'
// When the 'DIV' is clicked, toggle the 'green' and 'red' classes on all 'HEADER' elements using jQuery
$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('green red');
});
