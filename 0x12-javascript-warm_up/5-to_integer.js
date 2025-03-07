#!/usr/bin/env node
//printing first arg and converting it to Number

let arg = Number(process.argv[2])

if (isNaN(arg)) {
    console.log('Not a number');
} else {
     console.log(`My number: ${arg}`)
}
