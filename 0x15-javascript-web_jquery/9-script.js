// Wait for the document to be fully loaded and ready before executing the enclosed code
// Perform a GET request to the specified URL using jQuery's
$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
