#!/usr/bin/node
function factorial (number) {
  return number === 0 || isNaN(number) ? 1 : number * factorial(number - 1);
}

console.log(factorial(Number(process.argv[2])));
