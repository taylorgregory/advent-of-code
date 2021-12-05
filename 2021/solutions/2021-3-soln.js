// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-3-input.txt', 'utf8').split('\r\n'); // Keep as strings to keep leading zeros

// -- PART A (Answer = 3242606) -- //
// Task: 

let gammaArray = [];
let epsilonArray = [];
let idxTally;

// SOLUTION 1: 
// Aim: Simple loop through 
for (let idx = 0; idx < 12; idx++) {
    idxTally = 0;
    array.forEach((element) => {
        if (element[idx] == '1') {
            idxTally++;
        }
    });

    if (idxTally > array.length/2) {
        gammaArray[idx] = 1;
        epsilonArray[idx] = 0;
    } else {
        gammaArray[idx] = 0;
        epsilonArray[idx] = 1;
    }
}

const gammaRate = parseInt(gammaArray.join(''), 2);
const epsilonRate = parseInt(epsilonArray.join(''), 2);

console.log(gammaRate * epsilonRate);

// PART B:

let valueToKeep;

let filteredOxygenArr = array;
for (let idx = 0; idx < 12; idx++) {
    if (filteredOxygenArr.length > 1) {
        idxTally = 0;
        filteredOxygenArr.forEach((element) => {
            if (element[idx] == '1') {
                idxTally++;
            }
        });

        valueToKeep = (idxTally >= filteredOxygenArr.length/2) ? '1' : '0';
        filteredOxygenArr = filteredOxygenArr.filter((element) => { 
            if (element[idx] == valueToKeep) {
                return element;
            }
        });
    } else {
        break;
    }
}
const binaryOxygenGeneratorRating = filteredOxygenArr[0];
const decimalOxygenGeneratorRating = parseInt(binaryOxygenGeneratorRating, 2);

let filteredCarbonArr = array;
for (let idx = 0; idx < 12; idx++) {
    if (filteredCarbonArr.length > 1) {
        idxTally = 0;
        filteredCarbonArr.forEach((element) => {
            if (element[idx] == '1') {
                idxTally++;
            }
        });

        valueToKeep = (idxTally < filteredCarbonArr.length/2) ? '1' : '0';
        filteredCarbonArr = filteredCarbonArr.filter((element) => { 
            if (element[idx] == valueToKeep) {
                return element;
            }
        });
        console.log(filteredCarbonArr);
    } else {
        break;
    }
}

const binaryCarbonDioxideScrubberRating  = filteredCarbonArr[0];
const decimalCarbonDioxideScrubberRating = parseInt(binaryCarbonDioxideScrubberRating, 2);

console.log(decimalOxygenGeneratorRating * decimalCarbonDioxideScrubberRating);