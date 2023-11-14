#!/usr/bin/node

// To utilize the basis class import the Rectangle class.
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
