#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let result = 0;
request(url, (err, response, body) => {
  if (err) {
    console.log(url);
  }
  for (const i of JSON.parse(body).results) {
    for (const j of i.characters) {
      if (j.search('api/people/18/') > 0) {
        result += 1;
      }
    }
  }
  console.log(result);
});
