#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstInt = parseInt(process.argv[2], 10);
const secondInt = parseInt(process.argv[3], 10);

console.log(add(firstInt, secondInt));
