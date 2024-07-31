#!/usr/bin/env node
// script taht prints the number of movies by characterID

const request = require('request');
const apiUrl = process.argv[2];
const charID = 18;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const movieData = JSON.parse(body);
  let count = 0;
  movieData.results.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charID}/`)) {
      count++;
    }
  });
  console.log(count);
});
