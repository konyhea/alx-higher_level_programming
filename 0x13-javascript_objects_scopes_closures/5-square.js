#!/usr/bin/env node
// create a class and method

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || typeof w !== 'number' || h <= 0 || typeof h !== 'number') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}

module.exports = Square;
