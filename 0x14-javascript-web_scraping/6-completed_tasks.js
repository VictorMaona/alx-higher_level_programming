#!/usr/bin/node
// Send a request to the API URL provided.
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const taskList = JSON.parse(body);
  const userTotals = {};
  for (const task of taskList) {
    if (task.completed) {
      if (task.userId in userTotals) {
        userTotals[task.userId] += 1;
      } else {
        userTotals[task.userId] = 1;
      }
    }
  }
  console.log(userTotals);
});