#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let iterator = 0; iterator < x; iterator++) {
    console.log('C is fun');
  }
}
