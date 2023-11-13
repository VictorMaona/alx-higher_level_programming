#!/usr/bin/node

// Obtain the first parameter from the command line and try to turn it into an integer.
const x = Math.floor(Number(process.argv[2]));

// Verify whether the conversion produced a legitimate positive integer.
if (isNaN(x)) {
  // If the conversion fails, print "Missing number of occurrences"
  console.log('Missing number of occurrences');
} else {
  // Printing "C is fun" x times in a loop
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
