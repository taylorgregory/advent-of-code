// SETUP
// Reading the input file
const fs = require('fs');
array = fs.readFileSync('../inputs/2022-2-input.txt', 'utf8').split('\n');

// ------------------------------------------------------------------------------------------------------------------------------------------------------- //

// -- PART A (Answer = 10941) -- //
// Task: __

// A and X = rock
// B and Y = paper 
// C and Z = scissors

winLossObject = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3
};

moveObject = {
    'X': 1,
    'Y': 2,
    'Z': 3
};

myPoints = 0;

array.forEach(round => {
    myPoints += winLossObject[round] + moveObject[round[2]];
});

console.log(myPoints);

// -- PART B (Answer = 10941) -- //
// Task: __

lossObject = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

drawObject = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

winObject = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

myPoints = 0;

array.forEach(round => {
    if (round[2] == 'X') {
        myPoints += 0 + moveObject[lossObject[round[0]]]
    } else if (round[2] == 'Y') {
        myPoints += 3 + moveObject[drawObject[round[0]]]
    } else if (round[2] == 'Z') {
        myPoints += 6 + moveObject[winObject[round[0]]]
    }
});

console.log(myPoints);