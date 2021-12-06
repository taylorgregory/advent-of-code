const fs = require('fs');
array = fs.readFileSync('../inputs/2021-6-input.txt', 'utf8').split(',').map(Number); 

function simulateOneDayPassing (initialState) {
    let state = initialState.map((lanternfish) => {
        return lanternfish - 1;
    });

    let newLanternfish = [];
    state.forEach((lanternfish, index) => {
        if (lanternfish == -1) {
            state[index] = 6;
            newLanternfish.push(8);
        }
    });

    return state.concat(newLanternfish);
}

let state = array;

/*for (let i = 0; i < 80; i++) {
    state = simulateOneDayPassing(state);
} */

// for part b, we have to consider something different...
/*state = [1];
for (let i = 0; i < 256; i++) {
    state = simulateOneDayPassing(state);
    console.log(i);
}
 
console.log(state.length); */

// attempt number one.. just using the loop above.. didn't run

// attempt number 2.. separating into mini arrays of [0], [1] etc and trying to do some math from there. also didn't run

// attempt number 3.. writing a different algorithm
