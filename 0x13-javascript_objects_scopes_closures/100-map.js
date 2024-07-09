#!/usr/bin/node

const list = require('./100-data.js').list;

const mapNumber = list.map((value, index) => {
  return value * index;
});

console.log(list);
console.log(mapNumber);
