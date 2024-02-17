const { sign } = require("crypto");
const fs = require("fs");
array = fs.readFileSync("../inputs/2021-8-input.txt", "utf8").split("\r\n");

// PART A
// break up into an array of all final numbers
let allOutputValues = [];
array.forEach((line) => {
  outputValues = line.split("|")[1].trim().split(" ");
  allOutputValues.push(...outputValues);
});

let tallyOfUniqueNumbers = 0;
allOutputValues.forEach((value) => {
  if (
    value.length == 2 ||
    value.length == 4 ||
    value.length == 3 ||
    value.length == 7
  ) {
    tallyOfUniqueNumbers++;
  }
});

console.log(tallyOfUniqueNumbers);

// PART B

/*
0:    1:    2:    3:    4:
aaaa  ....  aaaa  aaaa  ....
b  c  .  c  .  c  .  c  b  c
b  c  .  c  .  c  .  c  b  c
....  ....  dddd  dddd  dddd
e  f  .  f  e  .  .  f  .  f
e  f  .  f  e  .  .  f  .  f
gggg  ....  gggg  gggg  ....

5:    6:    7:    8:    9:
aaaa  aaaa  aaaa  aaaa  aaaa
b  .  b  .  .  c  b  c  b  c
b  .  b  .  .  c  b  c  b  c
dddd  dddd  ....  dddd  dddd
.  f  e  f  .  f  e  f  .  f
.  f  e  f  .  f  e  f  .  f
gggg  gggg  ....  gggg  gggg
*/

// - digit 0 consists of 6 segments
// - digit 1 consists of 2 segments *
// digit 2 consists of 5 segments
// - digit 3 consists of 5 segments
// - digit 4 consists of 4 segments *
// digit 5 consists of 5 segments
// - digit 6 consists of 6 segments
// - digit 7 consists of 3 segments *
// - digit 8 consists of 7 segments *
// - digit 9 consists of 6 segments

let total = 0;
array.forEach((line) => {
  signalsAndOutputs = line.split("|");
  signals = signalsAndOutputs[0]
    .trim()
    .split(" ")
    .map((value) => value.split("").sort().join(""));

  signalLookupArray = [];
  for (let i = 0; i < 10; i++) {
    signalLookupArray[i] = "";
  }

  for (i = signals.length - 1; i >= 0; i--) {
    if (signals[i].length == 2) {
      signalLookupArray[1] = signals[i];
      signals.splice(i, 1);
    } else if (signals[i].length == 4) {
      signalLookupArray[4] = signals[i];
      signals.splice(i, 1);
    } else if (signals[i].length == 3) {
      signalLookupArray[7] = signals[i];
      signals.splice(i, 1);
    } else if (signals[i].length == 7) {
      signalLookupArray[8] = signals[i];
      signals.splice(i, 1);
    }
  }

  for (i = signals.length - 1; i >= 0; i--) {
    if (signals[i].length == 5) {
      numberOfLettersInFourPresent = 0;
      for (j = 0; j < 4; j++) {
        if (signals[i].includes(signalLookupArray[4][j])) {
          numberOfLettersInFourPresent++;
        }
      }

      if (
        signals[i].includes(signalLookupArray[1][0]) &&
        signals[i].includes(signalLookupArray[1][1])
      ) {
        signalLookupArray[3] = signals[i];
        signals.splice(i, 1);
      } else if (numberOfLettersInFourPresent == 3) {
        signalLookupArray[5] = signals[i];
        signals.splice(i, 1);
      } else {
        signalLookupArray[2] = signals[i];
        signals.splice(i, 1);
      }
    } else if (signals[i].length == 6) {
      if (
        signals[i].includes(signalLookupArray[4][0]) &&
        signals[i].includes(signalLookupArray[4][1]) &&
        signals[i].includes(signalLookupArray[4][2]) &&
        signals[i].includes(signalLookupArray[4][3])
      ) {
        signalLookupArray[9] = signals[i];
        signals.splice(i, 1);
      } else if (
        signals[i].includes(signalLookupArray[7][0]) &&
        signals[i].includes(signalLookupArray[7][1]) &&
        signals[i].includes(signalLookupArray[7][2])
      ) {
        signalLookupArray[0] = signals[i];
        signals.splice(i, 1);
      } else {
        signalLookupArray[6] = signals[i];
        signals.splice(i, 1);
      }
    }
  }

  outputs = signalsAndOutputs[1]
    .trim()
    .split(" ")
    .map((value) => value.split("").sort().join(""));

  outputAsString = '';
  outputs.forEach((output) => {
    outputAsString += signalLookupArray.indexOf(output);
  });
  total += parseInt(outputAsString);
});
console.log(total);

// PART C: playing with seven segment displays
// ------------------------------------------------- //
//      _          _        _      _  _   _          //
//  |_ |_| |_| |  | |  _   |    _ |_ |   | |  _ |_|  //
//  |_ | |  _| |_ |_| |    |_| |  |_ |_| |_| |   _|  //
//                                                   //
// ------------------------------------------------- //
