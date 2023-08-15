#!/usr/bin/node

// Increment the number
// Calls the provided function with the incremented number
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
