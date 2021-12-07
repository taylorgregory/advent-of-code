// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-7-input.txt', 'utf8').split(',').map(Number);

// brute force approach to task a
const maxValue = array.reduce(function(a, b) { return Math.max(a, b); });

let distanceArr = [];
for (let idx = 0; idx < maxValue; idx++) {
    let distanceVal = 0;
    for (let crabIdx = 0; crabIdx < array.length; crabIdx++) {
        distanceVal += Math.abs(array[crabIdx] - idx);
    }
    distanceArr[idx] = distanceVal;
}

const minValue = distanceArr.reduce(function(a, b) { return Math.min(a, b); });

console.log(minValue);
