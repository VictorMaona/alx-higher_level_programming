#!/usr/bin/node

// Obtain the first parameter from the command line and try to turn it into an integer.
const size = Math.floor(Number(process.argv[2]));

// Verify whether the conversion produced a legitimate positive integer.
if (isNaN(size)) {
  // If the conversion fails, print "Missing size"
  console.log('Missing size');
} else {
  // Go around every row.
  for (let r = 0; r < size; r++) {
    let row = '';
