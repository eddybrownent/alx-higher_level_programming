// Add a click event handler to the 'INPUT' element with the ID 'btn_translate'
// Perform a GET request to the API URL with the language code parameter
// Update the content of the div with property from the response data
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('div#hello').html(data.hello);
    });
  });
});
