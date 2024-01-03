#!/usr/bin/node
// Verify whether the episode number is given.
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
