#!/usr/bin/node

exports.esrever = function (list) {
  let newArr = [];
  let i = 0
  let len = list.length - 1
  while (len) {
    newArr[i] = list[len];
    len--;
    i++;
  }
  return newArr
};
