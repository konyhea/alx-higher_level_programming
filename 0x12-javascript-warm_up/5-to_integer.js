#!/usr/bin/node

const args = process.argv[2];
const parsedNumber = parseInt(args);

if (isNaN(parsedNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedNumber}`);
}
