#!/usr/bin/node

// FS module import for file system functions
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
