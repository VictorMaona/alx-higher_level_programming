#!/usr/bin/node

// Define Rectangle class
module.exports = class Rectangle {
  // Constructor acceptable parameters for height and width
  constructor(w, h) {
    // Verify if w and h are both positive integers.
    if (w > 0 && h > 0) {
      // Assignment of destructuring to initialize the width and height properties
      [this.width, this.height] = [w, h];
    }
  }
};
