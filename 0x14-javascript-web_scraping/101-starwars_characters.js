#!/usr/bin/enode
// characters of star wars Movie
const request = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

request(apiUrl, async (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);

  for (const charURL of result.characters) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, r, body) => {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
