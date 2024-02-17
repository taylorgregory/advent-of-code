const fs = require("fs");
array = fs
  .readFileSync("../inputs/2021-9-input.txt", "utf8")
  .split("\r\n")
  .map((row) => row.split("").map(Number));

// PART A:
let sumOfRiskLevels = 0;

for (i = 0; i < array.length; i++) { // rows
  for (j = 0; j < array[i].length; j++) { // columns
    currentVal = array[i][j];

    // no number greater than 9, so set to 10 so the check 'works'?
    upVal = i > 0 ? array[i - 1][j] : 10;
    downVal = i < array.length - 1? array[i + 1][j]  : 10;
    leftVal = j > 0 ? array[i][j-1] : 10;
    rightVal = j < array[i].length - 1 ? array[i][j+1] : 10;

    if (currentVal < upVal && currentVal < downVal && currentVal < leftVal && currentVal < rightVal) {
        sumOfRiskLevels += currentVal + 1;
    }
  }
}

console.log(sumOfRiskLevels);

/* Big ol unfinished draft.... do not critique too harshly... 
// PART B: 
arrayOfBasinSizes = [];
for (i = 0; i < array.length; i++) { // rows
    for (j = 0; j < array[i].length; j++) { // columns
        if (array[i][j] != 9) {
            currentBasinSize = array[i][j];
            array[i][j] = 9; // assigning this value to 9 so it is never considered in another basin

            rowIdxToCheck = i;
            columnIdxToCheck = j;

            scanningLeft = true;
            while (scanningLeft) {
                
                currentBasinSize = array[rowIdxToCheck][columnIdxToCheck];
                array[i][j] = 9; // assigning this value to 9 so it is never considered in another basin

                if (array[rowIdxToCheck][columnIdxToCheck] == 9) {
                    scanningLeft = false;
                    break;
                } else {

                }
            }

            scanningRight = true;
            while (scanningRight) {

            }

            

            stillInCurrentBasin = true;

        }
    }
} */
