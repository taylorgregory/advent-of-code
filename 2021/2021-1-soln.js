// [Add description here]

// SETUP
// Reading the input file
const fs = require('fs')
array = fs.readFileSync('2021-1-input.txt', 'utf8').split('\n').map(Number);

// -- PART A (Answer = 1448) -- //
// SOLUTION 1: 
let counter1 = 0;
for (let idx = 0; idx < (array.length - 1); idx++) { // Ending the loop at array.length - 1 as this is when there is nothing left to compare
    if (array[idx] < array[idx + 1]) {
        counter1++;
    }
}
console.log(counter1);

// SOLUTION 2: 
// TBC

/* sample python solution

# solution 2:
# aim: have two arrays (arr1 and arr2)
# trim the first element of arr1 and the last element of arr2
# arr1 - arr2
# if positive number, let value = 1, else, value = 0

# 1
# 2 1
# 3 2
# 4 3
#   4

# converting array of strings to array of numbers
arr1 = np.delete(array, 0)
arr2 = np.delete(array, len(array) - 1)

diff_arr = arr1 - arr2

bool_diff_arr = np.zeros(len(diff_arr))

for idx, val in enumerate(diff_arr):
    if val > 0:
        bool_diff_arr[idx] = 1

print(sum(bool_diff_arr))


*/

// -- PART B (Answer = 1471) -- //
// SOLUTION 1: 
let counter2 = 0;
let thisSum;
let nextSum = array[0] + array[1] + array[2]; // Initialising the next sum before entering the loop

for (let idx = 0; idx < (array.length - 3); idx++) { // Ending the loop at array.length - 3 as this is when there is nothing left to compare
    thisSum = nextSum;
    nextSum = array[idx + 1] + array[idx + 2] + array[idx + 3];
    if (nextSum > thisSum) {
        counter2++;
    }
}
console.log(counter2);

// SOLUTION 2:
// TBC