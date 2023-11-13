#!/usr/bin/node

// Using the designated prototype, define the add function.
function add(a, b) {
  return a + b;
}

// Retrieve and convert the first and second command-line inputs to numbers.
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

// After using transformed parameters to invoke the add method, print the outcome.
console.log(add(num1, num2));
