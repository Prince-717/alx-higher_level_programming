#!/usr/bin/node
const dict = require('./101-data.js').dict;
const freshDict = {};
for (const key in dict) {
  if (freshDict[dict[key]] === undefined) {
    freshDict[dict[key]] = [key];
  } else {
    freshDict[dict[key]].push(key);
  }
}
console.log(freshDict);
