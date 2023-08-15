#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let iterator = 0; iterator < x; iterator++) {
    let k = 0;
    let Variable = '';

    while (k < x) {
      Variable = Variable + 'X';
      k++;
    }
    console.log(Variable);
  }
}
