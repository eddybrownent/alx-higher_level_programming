// Perform a GET request to the specified URL using jQuery's
// update the content of the 'UL' element with the ID 'list_movies'
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
  });
});
