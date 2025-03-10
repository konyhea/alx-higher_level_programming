#!/usr/bin/env node
// printing x for a number of times
const size = Number(process.argv[2])

if (Number.isNaN(size) || size <= 0) {
    console.log('Missing size')
    process.exit(1)
//   return;
} else {
     for(let i = 0; i < size; i++) {
       console.log('X'.repeat(size))
}
}
