#!/usr/bin/node
// Script to fetch and write webpage content to a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, { encoding: 'utf-8' }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(filePath, body, (err) => {
    if (err) {
      console.log('Error writing to file:', err);
    }
  //      console.log('Data successfully written to', filePath);
  });
});
