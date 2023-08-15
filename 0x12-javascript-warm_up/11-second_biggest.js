#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const pars = process.argv
    .map(Number)
    .slice(2, process.argv.length)
    .sort((num1, num2) => num1 - num2);
  console.log(pars[pars.length - 2]);
}
