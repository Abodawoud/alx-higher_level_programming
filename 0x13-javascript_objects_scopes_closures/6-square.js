#!/usr/bin/node
const PreSquare = require('./5-square.js');

class Square extends PreSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let rows = this.size;
      while (rows) {
        console.log(c.repeat(this.size));
        rows--;
      }
    }
  }
}

module.exports = Square;
