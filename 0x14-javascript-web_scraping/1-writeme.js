#!/usr/bin/node

// Require the 'fs' module
const fs = require('fs');

// Getting filename from the CL
const filename = process.argv[2];
const content = process.argv[3];

// Read the file using 'utf-8' encoding
fs.writeFile(filename, content, 'utf-8', (error) => {
  // Check if an error occurred
  if (error) {
    console.log(error);
  }
});
