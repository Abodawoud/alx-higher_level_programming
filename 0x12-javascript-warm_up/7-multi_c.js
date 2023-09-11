#!/usr/bin/node
const { argv } = require('process');
const log = console.log;
let num = Number(argv[2]);

if (isNaN(num) || argv.length === 2) {
  log('Missing number of occurrences');
} else {
  while (num !== 0) {
    if (num < 0) {
      break;
    }
    log('C is fun');
    num--;
  }
}
