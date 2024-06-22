#!/usr/bin/node

function add (a, b) {
  const firstInt = parseInt(a, 10);
  const secInt = parseInt(b, 10);

  console.log(firstInt + secInt);
}

const length = process.argv.length;

if (length < 4) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
