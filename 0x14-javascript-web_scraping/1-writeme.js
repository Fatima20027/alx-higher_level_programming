#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

try {
  fs.writeFileSync(filePath, string, 'utf-8');
} catch (err) {
  console.error(err); // Print the error object
  process.exit(1);
}
