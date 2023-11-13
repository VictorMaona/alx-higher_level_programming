#!/usr/bin/node

// Determine how many command line parameters there are.
const count = process.argv.length;

// Check amount of parameters and display the relevant message by using the ternary operator.
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
