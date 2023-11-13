#!/usr/bin/node

// Verify that the first command-line argument's type is 'undefined'
console.log(
  typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]
);
