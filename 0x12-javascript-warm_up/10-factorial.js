#!/usr/bin/env node
// Function to calculate factorial recursively

let n = Number(process.argv[2]); // Convert input to a number

function factorial(num) {
   if (isNaN(num) || num < 0) return 1; // Handle invalid and negative inputs
   return num <= 1 ? 1 : num * factorial(num - 1);
}

console.log(factorial(n));
