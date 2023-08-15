#!/usr/bin/node

let iterator = 0;

exports.logMe = function count (item) {
  console.log(`${iterator}: ${item}`);
  iterator += 1;
};
