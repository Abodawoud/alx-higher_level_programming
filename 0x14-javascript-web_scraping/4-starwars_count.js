#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const character = films.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(character.length);
  }
});
