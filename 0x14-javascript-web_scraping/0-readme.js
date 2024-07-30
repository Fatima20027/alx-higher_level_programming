#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

try {
    const readMe = fs.readFileSync(filePath, 'utf-8');
    console.log(readMe);
} catch (err) {
    console.error(err); // Print the error object
    process.exit(1);
}
