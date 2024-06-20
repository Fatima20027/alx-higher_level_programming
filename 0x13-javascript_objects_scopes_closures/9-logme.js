#!/usr/bin/node

exports.logMe = function (item) {
  // prints the number of arguments already printed and the new argument value
  let count = 0;
  return function (item) {
    console.log(`${count}: ${item}`);
    count++;
  };
};
