#!/usr/bin/node

const { argv } = require('process');
const num = argv.slice(2).map(arg => Number(arg));
const log = console.log;

if (argv.length === 2 || argv.length === 3) {
  log(0);
} else {
  const arg = [...num].sort((a, b) => a - b);
  log(arg[arg.length - 2]);
}
