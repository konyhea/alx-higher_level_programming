#!/usr/bin/node

const argsLen = process.argv.length;

if (argsLen < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}