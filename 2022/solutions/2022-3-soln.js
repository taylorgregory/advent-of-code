// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2022-3-input.txt', 'utf8').split('\n');

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

// -- PART A (Answer = 7990) -- //

// Surely there is a nicer way of doing this...........
prioritiesObject = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
};

prioritiesTotal = 0;

array.forEach(rucksack => {
    firstPocket = rucksack.slice(0, rucksack.length/2)
    secondPocket = rucksack.slice(rucksack.length/2, rucksack.length)

    for (i = 0; i < firstPocket.length; i++) {
        if (secondPocket.includes(firstPocket[i])){
            prioritiesTotal += prioritiesObject[firstPocket[i]];
            break;
        }
    }
});

console.log(prioritiesTotal);

// -- PART B (Answer = ) -- //

prioritiesTotal = 0;

for (i = 0; i < array.length - 1; i+=3){
    for (j = 0; j < array[i].length; j++) {
        if(array[i+1].includes(array[i][j]) && array[i+2].includes(array[i][j])){
            prioritiesTotal += prioritiesObject[array[i][j]];
            break;
        } 
    } 
}

console.log(prioritiesTotal);