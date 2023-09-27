#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(fileName, body, { flag: 'w' }, err => {
    if (err) { console.log(err); }
  });
});
