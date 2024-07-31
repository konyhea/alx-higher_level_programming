#!/usr/bin/node
// find the scount
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const jsonBody = JSON.parse(body);
  let count = 0;
  for (const result of jsonBody.results) {
    for (const charURL of result.characters) {
      if (charURL.includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
