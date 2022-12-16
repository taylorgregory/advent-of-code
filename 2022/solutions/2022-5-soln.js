// SETUP
// Reading the input file
const fs = require('fs');

// -- TODO: read this in and transform it properly properly
//inputStacks = fs.readFileSync('../inputs/2022-5-input-stacks.txt', 'utf8').split('\n');
stackArray = [
    ['B', 'S', 'V', 'Z', 'G', 'P', 'W'],
    ['J', 'V', 'B', 'C', 'Z', 'F'],
    ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
    ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
    ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
    ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
    ['L', 'G', 'C', 'Z', 'V'],
    ['N', 'L', 'G'],
    ['J', 'F', 'H', 'C']
]

moves = fs.readFileSync('../inputs/2022-5-input-moves.txt', 'utf8').split('\n');

moves.forEach(move => {

    decodedMove = move.replace('move ', '').replace('from ', '').replace('to ', '').split(' ');
    quantityToMove = decodedMove[0];
    originalStack = stackArray[decodedMove[1] - 1];
    //newStack = stackArray[decodedMove[2] - 1];

    itemsToMove = originalStack.slice(originalStack.length - quantityToMove, originalStack.length);

    // Uncomment for part a
    /*for (i = itemsToMove.length - 1; i >= 0; i--){
        stackArray[decodedMove[2] - 1].push(itemsToMove[i]);
        stackArray[decodedMove[1] - 1].pop()
    } */

    itemsToMove.forEach(item => {
        stackArray[decodedMove[2] - 1].push(item);
        stackArray[decodedMove[1] - 1].pop()
    })
});

resultingString = '';

stackArray.forEach(stack => {
    resultingString += stack[stack.length - 1]
});

console.log(resultingString);

