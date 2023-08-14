#!/usr/bin/node

let n = Number(process.argv[2]);
if (!n) {
  console.log('Missing size');
} else {
  let str = '';
  let size = n;
  while (n > 0) {
    str += 'X';
    n--;
  }

  while (size > 0) {
    console.log(str);
    size--;
  }
}
