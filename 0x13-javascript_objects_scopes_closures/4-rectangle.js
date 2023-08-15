#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // exchanges the width and height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // multiplies the width and height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
