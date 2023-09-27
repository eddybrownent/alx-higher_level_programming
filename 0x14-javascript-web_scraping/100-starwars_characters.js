#!/usr/bin/node

// Imports request module requests
const request = require('request');

// Getting  Movie ID from CL
const movieId = process.argv[2];

// API URL for movies
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make HTTP GET request
request.get(apiUrl, { json: true }, (error, response, movie) => {
  if (error) {
    // if errors
    console.error(error);
    return;
  }

  // Print title of movie
  console.log(movie.title);

  // Loop character URLs in the movie
  movie.characters.forEach((characterUrl) => {
    request.get(characterUrl, { json: true }, (charError, charResponse, character) => {
      if (charError) {
        // if errors
        console.error(charError);
        return;
      }

      // Print name of character
      console.log(character.name);
    });
  });
});
