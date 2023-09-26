#!/usr/bin/node

// Require the 'fs' module
const fs = require('fs');

// Geting the filename from the CL
const filename = process.argv[2];

// Reading the file using 'utf-8' encoding
fs.readFile(filename, 'utf-8', (error, content) => {
// Check if there is error
  if (error) {
    console.log(error);
  } else {
    // If no error occurred, print the content
    console.log(content);
  }
});
