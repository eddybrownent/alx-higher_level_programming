#!/usr/bin/node

// Importing 'request' library
const request = require('request');

// Getting  the API URL from CL
const apiUrl = process.argv[2];

// Defines the character id to look for
const targetCharacterId = '18';

let movieCount = 0;

// Sending GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);

    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(targetCharacterId)) {
          movieCount += 1;
        }
      });
    });
    console.log(movieCount);
  }
});
