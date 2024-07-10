#!/usr/bin/node

const dict = require('./100-data.js');

const newDict = {};

for (const key in dict) {
  const occurrences = dict[key];

  if (newDict[occurrences] === undefined) {
    newDict[occurrences] = [key];
  } else {
    newDict[occurrences].push(key);
  }
}

console.log(newDict);
