#!/usr/bin/node

// Use recursion to define the factorial function.
function factorial(n) {
  // Base case: factorial of 0 is 1
  // Also handle the case when n is NaN, return 1 in such a case
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

// Obtain the command-line option and change its value to a number.
const num = Number(process.argv[2]);

// After using the translated parameter to invoke the factorial function, print the outcome.
console.log(factorial(num));
