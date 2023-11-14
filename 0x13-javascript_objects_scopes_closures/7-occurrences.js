#!/usr/bin/node

// Function to determine how many times the searchElement appears in the list
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
