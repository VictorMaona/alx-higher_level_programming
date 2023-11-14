#!/usr/bin/node

// Describe the class Rectangle.
module.exports = class Rectangle {
  // Constructor acceptable parameters for height and width
  constructor(w, h) {
    this.width = w; // Assign the supplied 'w' argument value to width attribute.
    this.height = h; // Assign the value of supplied 'h' argument to height attribute.
  }
};
