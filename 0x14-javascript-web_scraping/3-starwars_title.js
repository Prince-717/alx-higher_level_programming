#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
