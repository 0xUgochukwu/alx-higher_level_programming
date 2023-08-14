#!/usr/bin/node

let n = Number(process.argv[2]);
if (!n) {
  console.log('Missing number of occurences');
} else {
  while (n > 0) {
    console.log('C is fun');
    n--;
  }
}
