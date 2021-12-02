// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-2-input.txt', 'utf8').split('\r\n');

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