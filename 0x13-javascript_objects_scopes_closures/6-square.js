#!/usr/bin/node
const PreSquare = require('./5-square.js');

class Square extends PreSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let rows = this.width;
      while (rows) {
        console.log(c.repeat(this.width));
        rows--;
      }
    }
  }
}

module.exports = Square;
