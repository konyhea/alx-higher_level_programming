#!/usr/bin/node
// script that writes to a file

const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.log(err);
  }

//    console.log("Data written to");
});
