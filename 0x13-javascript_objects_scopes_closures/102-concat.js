#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];

// accessing content inside the file
const contentOne = fs.readFileSync(file1);
const contentTwo = fs.readFileSync(file2);

const contentNew = contentOne + contentTwo;

fs.writeFile(process.argv[4], contentNew, 'utf-8', (err) => {
  if (err) {
    throw err;
  }
});
