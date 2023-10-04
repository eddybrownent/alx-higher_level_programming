// Add a click event handler to the 'DIV' element with the ID 'add_item'
// When the 'DIV' is clicked, append a new 'li' element with the text 'Item' to the 'UL' element with the class 'my_list' using jQuery
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
