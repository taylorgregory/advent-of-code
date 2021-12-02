// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-2-input.txt', 'utf8').split('\r\n');

// -- PART A (Answer = 1694130) -- //
let distance = 0;
let depth = 0;

array.forEach((element) => {
    if (element.includes('forward')) {
        distance += parseInt(element.split(' ')[1]);
    } else if (element.includes('up')) {
        depth -= parseInt(element.split(' ')[1]);
    } else if (element.includes('down')) {
        depth += parseInt(element.split(' ')[1]);
    }
});

console.log(distance * depth);

// -- PART B (Answer = 1698850445) -- //
let newDistance = 0;
let newDepth = 0;
let aim = 0;

array.forEach((element) => {
    if (element.includes('forward')) {
        newDistance += parseInt(element.split(' ')[1]);
        newDepth += aim * parseInt(element.split(' ')[1]);
    } else if (element.includes('up')) {
        aim -= parseInt(element.split(' ')[1]);
    } else if (element.includes('down')) {
        aim += parseInt(element.split(' ')[1]);
    }
});

console.log(newDistance * newDepth);
