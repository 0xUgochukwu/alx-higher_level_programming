#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const item of list) {
    if (item === searchElement) {
      n += 1;
    }
  }
  return n;
};
