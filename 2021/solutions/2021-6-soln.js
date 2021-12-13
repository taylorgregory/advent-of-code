const fs = require('fs');
const array = fs.readFileSync('../inputs/2021-6-input.txt', 'utf8').split(',').map(Number); 

// initialising an empty array
let array2 = [];
for (let i = 0; i < 9; i++) {
    array2[i] = 0;
}

array.forEach((value) => {
    array2[value]++;
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
let state = array2;
for (let i = 0; i < 80; i++) {
    state = simulateOneDayPassing(state);
} 
console.log(state.length); 

// PART B
let state2 = array2;
for (let i = 0; i < 256; i++) {
    state2 = simulateOneOtherDayPassing(state2);
} 
console.log(state2.reduce((a, b) => a + b, 0));
