#!/usr/bin/node

// Export 'addMeMaybe' function.
exports.addMeMaybe = function (number, theFunction) {
  // Increase "number" by 1 then use modified value to invoke specified function.
  theFunction(++number);
};
