#!/usr/bin/node

/**
 * Define the Rectangle class.
 */
module.exports = class Rectangle {
  /**
   * The Rectangle class constructor.
   * @param {number} w - Width of the rectangle.
   * @param {number} h - Height of the rectangle.
   */
  constructor(w, h) {
    // Verify if w and h are both positive integers.
    if (w > 0 && h > 0) {
      // Assignment of destructuring to initialize width and height
      [this.width, this.height] = [w, h];
    }
  }

  /**
   * Instance method to print the rectangle with 'X' character.
   */
  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
