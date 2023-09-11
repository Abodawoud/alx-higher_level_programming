#!/usr/bin/node
const { argv } = require('process');
const log = console.log;
let num = Number(argv[2]);

if (isNaN(num) || argv.length === 2 || num < 0) {
  log('Missing number of occurrences');
} else {
  while (num !== 0) {
    log('C is fun');
    num--;
  }
}
