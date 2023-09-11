#!/usr/bin/node

const { argv } = require('process');
const log = console.log;

if (argv.length == 2) {
  log('No argument');
} else {
  log('Argument found');
}
