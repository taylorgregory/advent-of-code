// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-10-input.txt', 'utf8').split('\n');

const bracketObj = {
   hey: 3,
   ')': 57,
   '}': 1197,
   '>': 25137
};

console.log(bracketObj.hey);