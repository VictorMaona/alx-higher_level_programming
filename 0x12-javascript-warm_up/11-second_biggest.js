#!/usr/bin/node

// Verify whether the quantity of command-line parameters is three or fewer.
if (process.argv.length <= 3) {
  // If there are not enough parameters, print 0.
  console.log(0);
} else {
  // Convert command-line parameters to integers and slice to exclude the script name
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    // Arrange the digits in a rising order.
    .sort((a, b) => a - b);
  
  // Print the second-biggest integer, or the second-to-last element.
  console.log(args[args.length - 2]);
}
