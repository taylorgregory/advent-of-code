// SETUP
// Reading the input files
const fs = require('fs');
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
function checkOffNumberOnBoards (number, playingToWin = true) {
    let winningBoards = [];
    for (let i = 0; i < bingoBoards.length; i++) {
        for (let j = 0; j < bingoBoards[i].length; j++) {
            for (let k = 0; k < bingoBoards[i][j].length; k++) {
                if (bingoBoards[i][j][k] == number) {
                    bingoBoardsMap[i][j][k] = 1;
                    let winningBoard = checkIfWon(i, j, k);
                    if (winningBoard) {
                        winningBoards.push(winningBoard);
                        if (playingToWin) {
                            return winningBoards;
                        }
                    }
                }
            }
        }
    }
    return winningBoards;
}

function checkIfWon(boardNumber, rowNumber, columnNumber) {
    rowTotal = bingoBoardsMap[boardNumber][rowNumber].reduce((a, b) => a + b, 0);
    if (rowTotal == 5) {
        return boardNumber;
    }

    let boardColumnTotal = 0;
    for (boardRowIdx = 0; boardRowIdx < bingoBoardsMap[boardNumber].length; boardRowIdx++) {
        boardColumnTotal += bingoBoardsMap[boardNumber][boardRowIdx][columnNumber];
        if (boardColumnTotal == 5) {
            return boardNumber;
        }
    }
    return null;
}

function calculateFinalScore(boardIdx, numberDrawn) {
    remainingNumbersTotal = 0;
    for (j = 0; j < bingoBoardsMap[boardIdx].length; j++) {
        for (k = 0; k < bingoBoardsMap[boardIdx][j].length; k++) {
            if (bingoBoardsMap[boardIdx][j][k] == 0) {
                remainingNumbersTotal += bingoBoards[boardIdx][j][k];
            }
        }
    }
    return remainingNumbersTotal * numberDrawn;
}

function completePartA() {
    for (let i = 0; i < numbersDrawn.length; i++) {
        winningBoard = checkOffNumberOnBoards(numbersDrawn[i]);
        if (winningBoard.length > 0) {
            console.log(calculateFinalScore(winningBoard[0], numbersDrawn[i]));
            break;
        }
    }
}

function completePartB() {
    for (let i = 0; i < numbersDrawn.length; i++) {
        winningBoardIdx = checkOffNumberOnBoards(numbersDrawn[i], false);
        if (winningBoardIdx.length > 0) {
            if (bingoBoards.length > 1) {
                for (j = winningBoardIdx.length - 1; j >= 0; j--){
                    console.log(bingoBoardsMap[winningBoardIdx[j]]);
                    bingoBoards.splice(winningBoardIdx[j], 1);               
                    bingoBoardsMap.splice(winningBoardIdx[j], 1);
                }
                console.log(bingoBoards);
            } else {
                console.log(calculateFinalScore(winningBoardIdx[0], numbersDrawn[i]));
            }
        }
    }
}

completePartA();
completePartB();