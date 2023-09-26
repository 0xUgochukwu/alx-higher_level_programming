#!/usr/bin/node

const request = require('request');
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      if (film.characters.includes(character)) {
        count++;
      }
    });
    console.log(count);
  }
});
