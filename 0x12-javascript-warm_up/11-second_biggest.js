#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const ints = [];
  for (let i = 0; i < size; i++) {
    ints[i] = parseInt(process.argv[i + 2]);
  }
  ints.sort(function (a, b) { return b - a; });
  console.log(ints[1]);
}
