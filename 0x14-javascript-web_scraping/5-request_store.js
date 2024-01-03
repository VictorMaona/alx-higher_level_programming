#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Request the URL specified in the first command line argument.
request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
