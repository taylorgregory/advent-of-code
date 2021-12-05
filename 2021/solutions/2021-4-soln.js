// SETUP
// Reading the input files
const fs = require('fs');
const numbersDrawn = fs.readFileSync('../inputs/2021-4-input-numbersdrawn.txt', 'utf8').split(',').map(Number);

// Converting the string to arrays of arrays representing each bingo board
let bingoBoards = fs.readFileSync('../inputs/2021-4-input-bingoboards.txt', 'utf8').split('\r\n\r\n');
bingoBoards.forEach((element, index) => {
    bingoBoards[index] = element.split('\r\n');
    bingoBoards[index].forEach((value, idx) => {
        bingoBoards[index][idx] = bingoBoards[index][idx].replaceAll('  ', ' ').split(' ').map(Number);
    });
});

 /*
// Function which marks the given number off on every board
function checkOffNumberOnBoards (number) {
    bingoBoards.forEach((board, index) => {
        board.forEach((row, rowIndex) => {
            row.forEach((rowValue, rowValueIndex) => {
                if (rowValue == number) {
                    rowValue = '';
                }
            });
        });
    });
}

// Function which checks for any winning boards. Should only be called after the 5th number is drawn
function checkForWinningBoards() {

}



numbersDrawn.forEach((numberDrawn) => {
    checkOffNumberOnBoards(numberDrawn);

    // check if it won

    // if it won, calculate the sum

    // multiply the sum by the number
});

 */

