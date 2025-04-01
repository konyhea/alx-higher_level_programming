#!/uar/bin/env node
// crate a class and a method

class Rectangle {
  constructor(w, h) {
  if (w <= 0 || typeof w != 'number' || h <= 0 || typeof w != 'number') {
      return this;
}
   this.width = w;
   this.height = h;
}

    print() {
          for(let i = 0; i < this.height; i++) {
              console.log('X'.repeat(this.width));
}
}
}

module.exports = Rectangle

