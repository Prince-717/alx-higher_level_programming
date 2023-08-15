#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let iterator = 0; iterator < this.height; iterator++) console.log(c.repeat(this.width));
    }
  }
};
