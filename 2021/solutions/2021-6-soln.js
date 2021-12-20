const fs = require('fs');
const array = fs.readFileSync('../inputs/2021-6-input.txt', 'utf8').split(',').map(Number); 

// Compacting the original array into an array of fixed size that just tallies quantities
let compactArr = [];
for (let i = 0; i < 9; i++) {
    compactArr[i] = 0;
}
array.forEach((value) => {
    compactArr[value]++;
});

function simulateOneDayPassing (initialState) {
    let newState = [];
    newState[0] = initialState[1];
    newState[1] = initialState[2];
    newState[2] = initialState[3];
    newState[3] = initialState[4];
    newState[4] = initialState[5];
    newState[5] = initialState[6];
    newState[6] = initialState[0] + initialState[7];
    newState[7] = initialState[8];
    newState[8] = initialState[0];
    return newState;
}

// PART A
let partAState = compactArr;
for (let i = 0; i < 80; i++) {
    partAState = simulateOneDayPassing(partAState);
} 
console.log(partAState.length); 

// PART B
let partBState = compactArr;
for (let i = 0; i < 256; i++) {
    partBState = simulateOneDayPassing(partBState);
} 
console.log(partBState.reduce((a, b) => a + b, 0));
