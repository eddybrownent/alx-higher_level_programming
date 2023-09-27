#!/usr/bin/node

// Module for making HTTP requests
const request = require('request');

// Module for file system operations
const fs = require('fs');

// Get the URL and file name from CL
const url = process.argv[2];
const file = process.argv[3];

// Send an HTTP GET request to URL
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // If the request is successful, write the response body to a file
    fs.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
