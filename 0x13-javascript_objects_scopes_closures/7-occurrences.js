#!/usr/bin/ode

exports.nbOccurences = function (list, searchElement) {
  let identicalElements = 0; // Corrected variable name
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { // Use strict equality === to compare
      identicalElements++;
    }
  }

  return identicalElements;
};
