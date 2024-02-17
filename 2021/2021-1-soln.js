// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-1-input.txt', 'utf8').split('\n').map(Number);

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

// -- PART A (Answer = 1448) -- //
// Task: Count the number of times a depth measurement increases from the previous measurement

// SOLUTION 1: 
// Aim: comparing the side by side elements in a single array loop
let counterA = 0;
for (let idx = 0; idx < (array.length - 1); idx++) { // Ending the loop at array.length - 1 as this is when there is nothing left to compare
    if (array[idx] < array[idx + 1]) {
        counterA++;
    }
}
console.log(counterA);

// SOLUTION 2: 
// Aim: have two arrays (arr1 and arr2) and trim the first element of arr1 and last element of arr 2. Side by size, these two arrays should look something like this:
// 2 1
// 3 2
// 4 3

// Now, with arr1 - arr2, we retrieve whether there was an increase or not. Specifically, we obtain this by seeing the sign of the resulting value
// From here, the resulting array can be mapped to an array of 0 and 1s, with 1 indicating that there was an increase
// To see the number of increases, simply sum the elements of the mapped array

const arr1 = array.slice(1, array.length);
const arr2 = array.slice(0, array.length - 1);
const diff_arr = arr1.map((val, idx) => { return val - arr2[idx] > 0 });
console.log(diff_arr.reduce((a, b) => a + b, 0));

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

// -- PART B (Answer = 1471) -- //
// Task: Count the number of times the sum of measurements in a three measurement sliding window increases from the previous sum

// SOLUTION 1: 
let counterB = 0;
let thisSum;
let nextSum = array[0] + array[1] + array[2]; // Initialising the next sum before entering the loop

for (let idx = 0; idx < (array.length - 3); idx++) { // Ending the loop at array.length - 3 as this is when there is nothing left to compare
    thisSum = nextSum;
    nextSum = array[idx + 1] + array[idx + 2] + array[idx + 3];
    if (nextSum > thisSum) {
        counterB++;
    }
}
console.log(counterB);

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

