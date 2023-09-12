#!/usr/bin/node
const PreSquare = require('./5-square.js');

class Square extends PreSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print('X');
    } else {
      super.print(c);
    }
  }
}

module.exports = Square;
