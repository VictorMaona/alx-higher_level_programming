#!/usr/bin/node

// Obtain the first parameter from the command line and try to turn it into a number.
const num = Math.floor(Number(process.argv[2]));

// Use isNaN() to determine whether the result is not a number.
// Print "Not a number" if it's not a number, and the formatted number otherwise.
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
