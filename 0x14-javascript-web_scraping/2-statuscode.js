#!/usr/bin/node

// Require the 'request' module
const request = require('request');

// Get the URL from the CL
const url = process.argv[2];

// Use the 'request.get' method to make an HTTP GET request
request.get(url, (error, response) => {
  // Check if an error occurred during the request
  if (error) {
    console.log(error);
  } else {
    // If there was no error
    console.log(`code: ${response.statusCode}`);
  }
});
