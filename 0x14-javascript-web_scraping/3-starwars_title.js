#!/usr/bin/node
// script that prints title of star wars

const request = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request.get(apiUrl, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(body.title);
});
