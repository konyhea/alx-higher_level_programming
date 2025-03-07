#!/usr/bin/env node

let repeat = Number(process.argv[2]);

if (isNaN(repeat)) {
    console.log('Missing number of occurences')
} else {
    for (let i = 0; i < repeat; i++ ) {
         console.log('C is fun');
    }
  }

