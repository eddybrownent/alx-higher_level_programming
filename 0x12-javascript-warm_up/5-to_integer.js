#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  const parsedArg = parseInt(arg);
  if (Number.isInteger(parsedArg)) {
    console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
} else {
  console.log('Not a number');
}
