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


// Function which marks the given number off on every board
function checkOffNumberOnBoards (number, inputBoardState) {
    inputBoardState.forEach((board, index) => {
        board.forEach((row, rowIndex) => {
            row.forEach((rowValue, rowValueIndex) => {
                if (rowValue == number) {
                    inputBoardState[index][rowIndex][rowValueIndex] = '';
                }
            });
        });
    });
    return inputBoardState;
}

// Function which checks for any winning boards. Should only be called after the 5th number is drawn
function checkForWinningBoards(inputBoardState) {
    // first check entire rows
    inputBoardState.forEach((board, boardIndex) => {

        // reduce to check for columns that win


        // reduce to check for rows that win
        //diff_arr.reduce((a, b) => a + b, 0)

        board.forEach((row, rowIndex) => {
            let numEmptyValuesInRow = 0;
            row.forEach((rowValue, rowValueIndex) => {
                if (rowValue == '') {
                    numEmptyValuesInRow++;
                }
            });
            console.log(numEmptyValuesInRow);

            if (numEmptyValuesInRow === 5) {
                return boardIndex;
            }
        });
    });
    return null;
    // then check entire columns
}


numbersDrawn.forEach((numberDrawn) => {
    bingoBoards = checkOffNumberOnBoards(numberDrawn, bingoBoards);
    result = checkForWinningBoards(bingoBoards);
    // check if it won


    console.log(result);
    // if it won, calculate the sum

    // multiply the sum by the number
});


 

