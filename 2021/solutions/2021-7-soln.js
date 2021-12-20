// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-7-input.txt', 'utf8').split(',').map(Number);

// brute force approach to task a (answer = 343605)
const maxValue = array.reduce(function(a, b) { return Math.max(a, b); });

let distanceArr = [];
for (let idx = 0; idx < maxValue; idx++) {
    distanceArr[idx] = 0;
    for (let crabIdx = 0; crabIdx < array.length; crabIdx++) {
        distanceArr[idx] += Math.abs(array[crabIdx] - idx);
    }
}

const minValue = distanceArr.reduce(function(a, b) { return Math.min(a, b); });
console.log(minValue);

// part b (answer = 96744904)

let distanceArr2 = [];
for (let idx = 0; idx < maxValue; idx++) {
    distanceArr2[idx] = 0;
    for (let crabIdx = 0; crabIdx < array.length; crabIdx++) {
        absVal = Math.abs(array[crabIdx] - idx);
        let fuelAmount = 0;
        for (let accumulatingFuel = 1; accumulatingFuel <= absVal; accumulatingFuel++) {
            fuelAmount += accumulatingFuel;
        }
        distanceArr2[idx] += fuelAmount;
    }
}

const minValue2 = distanceArr2.reduce(function(a, b) { return Math.min(a, b); });
console.log(minValue2);