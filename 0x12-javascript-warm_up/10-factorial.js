#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  } else if (number <= 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const fact = factorial(arg);

console.log(fact);
