#!/usr/bin/node
// script to display URL

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log('code:', response && response.statusCode);
});
