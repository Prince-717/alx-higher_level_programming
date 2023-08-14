#!/usr/bin/node
const varCount = process.argv.length;
console.log(varCount === 2 ? 'No argument' : varCount === 3 ? 'Argument found' : 'Arguments found');
