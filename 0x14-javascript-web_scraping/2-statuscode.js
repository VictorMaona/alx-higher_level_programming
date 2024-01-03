#!/usr/bin/node
// Verify whether the URL is given.
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
