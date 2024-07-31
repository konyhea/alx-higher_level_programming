#!/usr/bin/node
// script that finds characters in starsWars
const request = require('request');
const id = process.argv[2];
const apiUrl = ` https://swapi-api.alx-tools.com/api/films/${id}/`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const bodyContent = JSON.parse(body);

  for (const charUrl of bodyContent.characters) {
    request(charUrl, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }

      const name = JSON.parse(body);
      console.log(name.name);
    });
  }
});
