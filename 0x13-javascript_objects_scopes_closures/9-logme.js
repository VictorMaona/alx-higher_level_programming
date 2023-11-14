#!/usr/bin/node

// Variable to record how many arguments have already been printed
let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
