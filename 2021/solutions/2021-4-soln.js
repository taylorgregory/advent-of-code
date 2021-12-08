// SETUP
// Reading the input files
const fs = require('fs');
const { mainModule } = require('process');
const numbersDrawn = fs.readFileSync('../inputs/2021-4-input-numbersdrawn.txt', 'utf8').split(',').map(Number);

// Converting the string to arrays of arrays representing each bingo board
let bingoBoards = fs.readFileSync('../inputs/2021-4-input-bingoboards.txt', 'utf8').split('\r\n\r\n');
let bingoBoardsMap = [];
bingoBoards.forEach((element, index) => {
    bingoBoardsMap[index] = [];
    bingoBoards[index] = element.split('\r\n');
    bingoBoards[index].forEach((value, idx) => {
        bingoBoards[index][idx] = bingoBoards[index][idx].trim().replaceAll('  ', ' ').split(' ').map(Number);
        bingoBoardsMap[index][idx] = [0,0,0,0,0];
    });
});

// Function which marks the given number off on every board
function checkOffNumberOnBoards (number, boards, boardMap) {
    boards.forEach((board, index) => {
        board.forEach((row, rowIndex) => {
            row.forEach((rowValue, rowValueIndex) => {
                if (rowValue == number) {
                    boardMap[index][rowIndex][rowValueIndex] = 1;
                }
            });
        });
    });
    return boardMap;
}

// Function which checks for any winning boards. Should only be called after the 5th number is drawn
function checkForWinningBoards(boardMap) {
    for (boardIdx = 0; boardIdx < boardMap.length; boardIdx++) {
        let boardColumnTotals = [0,0,0,0,0];
        for (boardRowIdx = 0; boardRowIdx < boardMap[boardIdx].length; boardRowIdx++) {
            rowTotal = boardMap[boardIdx][boardRowIdx].reduce((a, b) => a + b, 0);
            if (rowTotal == 5) {
                return boardIdx;
            }
            for (boardRowValIdx = 0; boardRowValIdx < boardMap[boardIdx][boardRowIdx].length; boardRowValIdx++) {
                boardColumnTotals[boardRowValIdx] += boardMap[boardIdx][boardRowIdx][boardRowValIdx];
                if (boardColumnTotals[boardRowValIdx] == 5) {
                    return boardIdx;
                }
            }
        }
    }
    return null;
}

// 

function completePartA() {
    for (let i = 0; i < numbersDrawn.length; i++) {
    bingoBoardsMap = checkOffNumberOnBoards(numbersDrawn[i], bingoBoards, bingoBoardsMap);
    winningBoardIdx = checkForWinningBoards(bingoBoardsMap);
    if (winningBoardIdx) {
        remainingNumbersTotal = 0;
        for (j = 0; j < bingoBoardsMap[winningBoardIdx].length; j++) {
            for (k = 0; k < bingoBoardsMap[winningBoardIdx][j].length; k++) {
                if (bingoBoardsMap[winningBoardIdx][j][k] == 0) {
                    remainingNumbersTotal += bingoBoards[winningBoardIdx][j][k];
                }
            }
        }
        console.log(remainingNumbersTotal * numbersDrawn[i]);
        break;
    }
}