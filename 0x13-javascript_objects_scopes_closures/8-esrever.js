#!/usr/bin/node

// Function for reversing list without utilizing integrated reverse technique
exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
