#!/usr/bin/node
function argument () {
  if (process.argv.length <= 2) {
    console.log('No argument');
  } else {
    console.log('Argument found');
  }
}

argument();
