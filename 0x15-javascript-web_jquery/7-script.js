// Perform a GET request to the specified URL using jQuery's
// When the request is successful, update the text content of the 'DIV' element with the ID 'character' with the 'name' property from the response data
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  $('div#character').text(data.name);
});
