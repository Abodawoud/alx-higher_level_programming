#!/usr/bin/node

const { argv } = require('process');
const log = console.log;

if (argv.length === 2) {
  log('No argument');
} else if (argv.length === 3) {
  log('Argument found');
} else {
  log('Arguments found');
}
