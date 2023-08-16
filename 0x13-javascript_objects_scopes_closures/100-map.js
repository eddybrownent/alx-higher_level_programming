#!/usr/bin/node

// importing then converting it into an array
const list = require('./100-data.js').list;

console.log(list);

// use map to multiply each value with its index
const map1 = list.map((value, index) => value * index);

console.log(map1);
