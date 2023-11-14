#!/usr/bin/node
const args = process.argv;
if (args[2] == null) {
  console.log('Missing size');
} else {
  for (let row = 0; row < parseInt(args[2]); row++) {
    let rowString = '';
    for (let column = 0; column < parseInt(args[2]); column++) {
      rowString += 'X';
    }
    console.log(rowString);
  }
}
