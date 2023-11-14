#!/usr/bin/node

// Creates a converter function for the given base function
exports.converter = function (base) { return num => num.toString(base); };
