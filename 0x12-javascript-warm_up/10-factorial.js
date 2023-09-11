#!/usr/bin/node
const { argv } = require('process');
const log = console.log;
const num = Number(argv[2]);

function factorial (num) {
  if (isNaN(num) || argv.length === 2 || num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

log(factorial(num));
