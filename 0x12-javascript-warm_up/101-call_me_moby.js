#!/usr/bin/node

// 'callMeMoby' is function to export.
exports.callMeMoby = function (x, theFunction) {
  // Call the given function each time you iterate 'x' times.
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
