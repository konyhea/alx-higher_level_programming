#!/usr/bin/node

function factorial (a) {
  const num = parseInt(a, 10);
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

const args = process.argv[2];

console.log(factorial(args));
