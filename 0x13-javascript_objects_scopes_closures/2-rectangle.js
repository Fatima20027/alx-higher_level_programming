#!/usr/bin/node

module.exports = class Rectangle {
  // class Rectangle that defines a rectangle
  constructor (w, h) {
    // creates an empty object if w or h is equal to 0 or not a positive integer
    if ((w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
};
