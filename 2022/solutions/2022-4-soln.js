// SETUP
// Reading the input file
const fs = require('fs'); 
array = fs.readFileSync('../inputs/2022-4-input.txt', 'utf8').split('\n');

firstElf = array.map(item => item.split(',')[0])
secondElf = array.map(item => item.split(',')[1])

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

// -- PART A (Answer = 444) -- //
// Task: __

numFullOverlap = 0

for (i = 0; i < array.length; i++) {
    // If second range is contained within first range OR first range is contained within second range
    if ((parseInt(firstElf[i].split('-')[0]) >= parseInt(secondElf[i].split('-')[0]) && parseInt(firstElf[i].split('-')[1]) <= parseInt(secondElf[i].split('-')[1])) || 
        (parseInt(secondElf[i].split('-')[0]) >= parseInt(firstElf[i].split('-')[0]) && parseInt(secondElf[i].split('-')[1]) <= parseInt(firstElf[i].split('-')[1]))){
        numFullOverlap += 1;
    }
}

console.log(numFullOverlap);

// -- PART B (Answer = 801) --  //

numPartialOverlap = 0;

for (i = 0; i < array.length; i++) {
    // (elf1 a is less than  or equal to elf2 a AND elf1 b is greater than or equal to elf1 a) OR
    // (elf1 a is less then elf2 b AND elf1 b is greated than elf 2b)
    if ((parseInt(firstElf[i].split('-')[0]) <= parseInt(secondElf[i].split('-')[0]) && 
        parseInt(firstElf[i].split('-')[1]) >= parseInt(secondElf[i].split('-')[0])) ||
        (parseInt(firstElf[i].split('-')[0]) <= parseInt(secondElf[i].split('-')[1]) && 
        parseInt(firstElf[i].split('-')[1]) >= parseInt(secondElf[i].split('-')[1])) ||
        (parseInt(secondElf[i].split('-')[0]) <= parseInt(firstElf[i].split('-')[0]) && 
        parseInt(secondElf[i].split('-')[1]) >= parseInt(firstElf[i].split('-')[0])) ||
        (parseInt(secondElf[i].split('-')[0]) <= parseInt(firstElf[i].split('-')[1]) && 
        parseInt(secondElf[i].split('-')[1]) >= parseInt(firstElf[i].split('-')[1]))) {
            numPartialOverlap += 1;
    }
}

console.log(numPartialOverlap);