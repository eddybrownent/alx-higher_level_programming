#!/usr/bin/node

// Imports request for HTTP requests
const request = require('request');

// Gets the API URL from CL
const apiUrl = process.argv[2];

// Makes GET request to the URL using JSON response
request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    // if errors occur
    console.log(error);
    return;
  }

  // count of completed tasks by user ID
  const completedTaskCount = {};

  // Loop body array to count completed tasks
  body.forEach((todo) => {
    if (todo.completed) {
      // Check if user ID exists in completedTaskCount object
      if (!completedTaskCount[todo.userId]) {
        // If not count start from 1
        completedTaskCount[todo.userId] = 1;
      } else {
        // If yes add 1
        completedTaskCount[todo.userId] += 1;
      }
    }
  });

  // Print completed task count
  console.log(completedTaskCount);
});
