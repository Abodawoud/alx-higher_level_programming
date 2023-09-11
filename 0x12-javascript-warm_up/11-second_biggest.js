#!/usr/bin/node

const { argv } = require('process');
const num = argv.slice(2).map(arg => Number(arg));
const log = console.log;

if (argv.length === 2 || argv.length === 3) {
  log(0);
} else {
    log(Math.max(...num));
}
