#!/usr/bin/node

let count = 0;

// prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
