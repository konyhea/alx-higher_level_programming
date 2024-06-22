#!/usr/bin/node

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a <= 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

const args = process.argv[2];

console.log(factorial(args));
