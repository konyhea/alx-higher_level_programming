#!/usr/bin/env node
// printing the first argument using process.argv

let firstArg = process.argv[2]

if (firstArg) {
    console.log(firstArg);
} else {
    console.log('No argument')
}
