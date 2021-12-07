const fs = require('fs');
array = fs.readFileSync('../inputs/2021-6-input.txt', 'utf8').split(',').map(Number); 

// PART A
function simulateOneDayPassing (initialState) {
    let state = initialState.map((lanternfish) => {
        return lanternfish - 1;
    });

    let newLanternfish = [];
    state.forEach((lanternfish, index) => {
        if (lanternfish == -1) {
            state[index] = 6;
            newLanternfish.push(8);
        }
    });

    return state.concat(newLanternfish);
}

let state = array;
for (let i = 0; i < 80; i++) {
    state = simulateOneDayPassing(state);
    console.log(i);
} 
console.log(state.length); 

// PART B

// initialising an empty array
let partBArray = [];
for (let i = 0; i < 9; i++) {
    partBArray[i] = 0;
}

array.forEach((value) => {
    partBArray[value]++;
});

console.log(partBArray);

function simulateOneOtherDayPassing (initialState) {
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

state = partBArray;
for (let i = 0; i < 256; i++) {
    state = simulateOneOtherDayPassing(state);
} 

console.log(state.reduce((a, b) => a + b, 0));
