#!/usr/bin/node

function factorial (a) {
  if (a <= 0) {
    return 0;
  } else if (a === 1 || isNaN(a)) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const myInt = parseInt(process.argv[2]);
console.log(factorial(myInt));
