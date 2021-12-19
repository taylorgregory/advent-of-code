const fs = require('fs');
array = fs.readFileSync('../inputs/2021-8-input.txt', 'utf8').split('\r\n');

// digit 1 consists of 2 segments
// digit 4 consists of 4 segments
// digit 7 consists of 3 segments
// digit 8 consists of 7 segments

// PART A
// break up into an array of all final numbers
let allOutputValues = [];
array.forEach((line) => {
    outputValues = line.split('|')[1].trim().split(' ');
    allOutputValues.push(...outputValues);
});

let tallyOfUniqueNumbers = 0;
allOutputValues.forEach((value) => {
    if (value.length == 2 || value.length == 4 || value.length == 3 || value.length == 7) {
        tallyOfUniqueNumbers++;
    }
});

console.log(tallyOfUniqueNumbers);