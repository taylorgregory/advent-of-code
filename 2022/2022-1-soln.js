// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2022-1-input.txt', 'utf8').split('\n').map(Number);

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

// -- PART A (Answer = 70374) -- //
// Task: __

// Initialising maxCals to keep track of the current maximum calories
maxCals = 0

// Initialisign currentTotal to keep track of the current elf's calories
currentTotal = 0

array.forEach(foodCals => {
    if (foodCals == "") {
        if (currentTotal > maxCals) {
            maxCals = currentTotal
        }
        currentTotal = 0
    } else {
        currentTotal += foodCals
    }
});

console.log(maxCals)

// -- PART B (Answer = 204610) -- //

maxCalArray = {
    "first": 0,
    "second": 0,
    "third": 0
}

currentTotal = 0

array.forEach(foodCals => {
    if (foodCals == "") {
        if (currentTotal > maxCalArray["first"]) {
            maxCalArray["third"] = maxCalArray["second"]
            maxCalArray["second"] = maxCalArray["first"]
            maxCalArray["first"] = currentTotal
        } else if (currentTotal < maxCalArray["first"] && currentTotal > maxCalArray["second"]) {
            maxCalArray["third"] = maxCalArray["second"]
            maxCalArray["second"] = currentTotal
        } else if (currentTotal < maxCalArray["second"] && currentTotal > maxCalArray["third"]) {
            maxCalArray["third"] = currentTotal
        }

        currentTotal = 0
    } else {
        currentTotal += foodCals
    }
});

console.log(maxCalArray["first"] + maxCalArray["second"] + maxCalArray["third"])