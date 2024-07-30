#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const res = request.get(url);
res.on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
