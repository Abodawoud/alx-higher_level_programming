#!/usr/bin/node

const { argv } = require('process');
const log = console.log;
let i = 0;

while (argv[i]) {
  i++;
}
if (i === 2) {
  log('No argument');
} else {
  log(argv[2]);
}
