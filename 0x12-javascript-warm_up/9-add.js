#!/usr/bin/node
const { argv } = require('process');
const log = console.log;
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);

log(num1 + num2);
