#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
    [list[i], list[list.length - 1 - i]] = [list[list.length - 1 - i], list[i]];
  }
};


const myArray = [1, 2, 3, 4, 5];
exports.esrever(myArray);
