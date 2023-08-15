#!/usr/bin/node

const dict = require('./101-data').dict;

const userOccurrences = {};

for (const userID in dict) {
  const occurrence = dict[userID];

  if (!userOccurrences[occurrence]) {
    userOccurrences[occurrence] = [];
  }

  userOccurrences[occurrence].push(userID);
}

console.log(userOccurrences);
