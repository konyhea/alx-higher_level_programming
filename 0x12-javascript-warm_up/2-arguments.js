#!/usr/bin/node

const argsLen = process.argv.length;

if (argsLen < 3) {
  console.log('No argument');
} else if (argsLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
