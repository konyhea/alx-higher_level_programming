#!/usr/bin/env node
// handling args in proces.argv
let x = process.argv[1] 
return x ? console.log('Argument found') : console.log('No argument');

