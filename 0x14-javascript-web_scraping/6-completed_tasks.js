#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const doneTasks = {};
  const todos = JSON.parse(body);

  for (const i in todos) {
    if (todos[i].completed) {
      if (doneTasks[todos[i].userId] === undefined) {
        doneTasks[todos[i].userId] = 0;
      }
      doneTasks[todos[i].userId]++;
    }
  }
  console.log(doneTasks);
});
