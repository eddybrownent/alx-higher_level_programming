#!/usr/bin/node

const dict = require('./101-data.js').dict;

// console.log(dict);

const dictNew = {};

for (const userId in dict) {
  const count = dict[userId];

  if (!dictNew[count]) {
    dictNew[count] = [];
  }
  dictNew[count].push(userId);
}

console.log(dictNew);
