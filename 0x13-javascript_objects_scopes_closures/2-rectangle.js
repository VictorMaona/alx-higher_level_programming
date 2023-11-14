#!/usr/bin/node

// Describes the Rectangle class
module.exports = class Rectangle {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
};
