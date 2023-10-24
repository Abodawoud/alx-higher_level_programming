#!/usr/bin/node
const request = require('request');

request.get(`${process.argv[2]}?completed=true`, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const todos = JSON.parse(body);
  const completedTaskCount = {};

  todos.forEach((todo) => {
    const userId = todo.userId;
    const completed = todo.completed;

    if (completed) {
      if (completedTaskCount[userId]) {
        completedTaskCount[userId]++;
      } else {
        completedTaskCount[userId] = 1;
      }
    }
  });

  console.log(completedTaskCount);
});
