#!/usr/bin/node

// Bring the 'list' array in.
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
