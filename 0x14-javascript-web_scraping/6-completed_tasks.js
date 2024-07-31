#!/usr/bin/node
// script that computes number of tasks

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const completed = {};
  const taskContent = JSON.parse(body);
  for (const task of taskContent) {
    if (task.completed) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
