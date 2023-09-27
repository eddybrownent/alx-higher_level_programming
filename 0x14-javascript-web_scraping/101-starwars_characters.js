#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Movie ID from CL
const movieId = process.argv[2];

// Star Wars API URL for movies
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// HTTP GET request using jason
request.get(apiUrl, { json: true }, (error, response, movie) => {
  if (error) {
    console.error(error);
    return;
  }

  // Loop character URLs in same order as characters list
  movie.characters.forEach((characterUrl) => {
    request.get(characterUrl, { json: true }, (charError, charResponse, character) => {
      if (charError) {
        console.error(charError);
        return;
      }

      // Print name the character
      console.log(character.name);
    });
  });
});
