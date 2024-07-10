#!/usr/bin/node

const args = process.argv.slice(2);

// Convert all arguments to integers and sort them
const sortedArgs = args.map(arg => parseInt(arg)).sort((a, b) => a - b);

// Check conditions and print accordingly
if (args.length === 0 || args.length === 1) {
    console.log('0');
} else {
    // Access the second largest element (second from the end in sorted array)
    console.log(sortedArgs[sortedArgs.length - 2]);
}
