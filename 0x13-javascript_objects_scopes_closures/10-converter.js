#!/usr/bin/node

// The 'converter' function returns another function that takes a number
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
