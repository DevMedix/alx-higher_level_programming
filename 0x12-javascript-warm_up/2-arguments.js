#!/usr/bin/node
let args = process.argv;

if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else if (args > 3) {
  console.log('Arguments found');
}
