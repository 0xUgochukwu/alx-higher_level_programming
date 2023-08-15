#!/usr/bin/node

const dict = require('./101-data').dict;

const userOccurrences = {};

for (const occurrence in dict) {
  const userID = dict[occurrence];

  if (!userOccurrences[userID]) {
    userOccurrences[userID] = [];
  }

  userOccurrences[userID].push[occurrence];
};

console.log(userOccurrences);
