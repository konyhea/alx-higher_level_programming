#!/usr/bin/env node

exports.esrever = function (list) {
  const listLen = list.length;
  const newList = []; // Corrected variable name and added missing 'let'

  for (let i = listLen - 1; i >= 0; i--) { // Corrected loop initialization and condition
    newList.push(list[i]); // Corrected method name and added missing 'let'
  }

  return newList;
};
