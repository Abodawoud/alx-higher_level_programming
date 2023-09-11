#!/usr/bin/node

const { argv } = require('process');
const log = console.log;
const num = Number(argv[2]);

if (isNaN(num)) {
  log('Not a number');
} else {
  log(Math.floor(num));
}
