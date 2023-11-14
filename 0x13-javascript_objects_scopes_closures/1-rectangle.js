#!/usr/bin/node

// Describe the class Rectangle.
module.exports = class Rectangle {
  // Constructor acceptable parameters for height and width
  constructor(w, h) {
    // Set up instance properties initially.
    this.width = w; // Assign the supplied 'w' argument's value to width attribute.
    this.height = h; // Assign the value of supplied 'h' argument to height attribute.
  }
};
