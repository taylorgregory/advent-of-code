// SETUP
// Reading the input file
const fs = require("fs");
array = fs
  .readFileSync("../inputs/2021-10-input.txt", "utf8")
  .split("\n")
  .map((brackets) => brackets.split(""));

// PART A:
// Arrays to define points, opening brackets, closing brackets
const bracketPoints = [3, 57, 1197, 25137];
const openingBrackets = ["(", "[", "{", "<"];
const closingBrackets = [")", "]", "}", ">"];

// Need to define a 'stack' type array
let openingBracketStack = [];
let topOfBracketStack;
let bracketPointTotal = 0;

for (let i = 0; i < array.length; i++) {
  for (let j = 0; j < array[i].length; j++) {
    if (openingBrackets.indexOf(array[i][j]) >= 0) {
      openingBracketStack.push(array[i][j]);
    } else {
      topOfBracketStack = openingBracketStack[openingBracketStack.length - 1];
      if (openingBrackets.indexOf(topOfBracketStack) == closingBrackets.indexOf(array[i][j])) {
        openingBracketStack.pop();
      } else {
         bracketPointTotal += bracketPoints[closingBrackets.indexOf(array[i][j])];
        break;
      }
    }
  }
}

console.log(bracketPointTotal);
