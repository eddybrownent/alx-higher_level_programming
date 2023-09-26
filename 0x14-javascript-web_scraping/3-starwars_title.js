#!/usr/bin/node

// Require the 'request' module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API with the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the specified URL
request.get(url, (error, response, body) => {
  // Check if an error occurred
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response body
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
