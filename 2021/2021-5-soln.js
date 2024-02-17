// SETUP
const fs = require('fs');
array = fs.readFileSync('../inputs/2021-5-input.txt', 'utf8').split('\r\n'); 
array.forEach((coordinate, coordinateIdx) => {
    firstCoord = coordinate.split(' -> ')[0];
    secondCoord = coordinate.split(' -> ')[1];
    array[coordinateIdx] = [firstCoord.split(',')[0], firstCoord.split(',')[1], secondCoord.split(',')[0], secondCoord.split(',')[1]].map(Number);
});

// Commented out - this is for part A (answer = 5169)
/*// Filtering out the coordinates that do not form horizontal or vertical lines
array = array.filter((coordinate) => {
    return (coordinate[0] == coordinate[2]) || (coordinate[1] == coordinate[3])
}); */

// Initialise an empty 1000 X 1000 array
grid = [];
for (let i = 0; i < 1000; i++) {
    grid[i] = [];
    for (let j = 0; j < 1000; j++) {
        grid[i][j] = 0;
    }
}

array.forEach((coordinate) => {
    // if the first and third elements are equal, then the x values are equal and we are incrementing in the y direction
    // for example, if we are considering the case [1, 4, 1, 6] then we need to modify arr[4][1], arr[5][1], arr[6][1]
    if (coordinate[0] == coordinate[2]) {
        for (let value = Math.min(coordinate[1], coordinate[3]); value <= Math.max(coordinate[1], coordinate[3]); value++) {
            grid[value][coordinate[0]] += 1;
        }
    // the opposite is true for if the second and fourth elements are equal
    } else if (coordinate[1] == coordinate[3]) {
        for (let value = Math.min(coordinate[0], coordinate[2]); value <= Math.max(coordinate[0], coordinate[2]); value++) {
            grid[coordinate[1]][value] += 1;
        }
    // diagonal lines
    } else {
        // get how many coordinates there will be:
        numCoord = Math.abs(coordinate[0] - coordinate[2]) + 1;

        xCoords = [];
        if (coordinate[0] < coordinate[2]) {
            for (let i = coordinate[0]; i <= coordinate[2]; i++) {
                xCoords.push(i);
            }
        } else if (coordinate[0] > coordinate[2]) {
            for (let i = coordinate[0]; i >= coordinate[2]; i--) {
                xCoords.push(i);
            }  
        }

        yCoords = [];
        if (coordinate[1] < coordinate[3]) {
            for (let i = coordinate[1]; i <= coordinate[3]; i++) {
                yCoords.push(i);
            }
        } else {
            for (let i = coordinate[1]; i >= coordinate[3]; i--) {
                yCoords.push(i);
            }  
        }

        for (coordIdx = 0; coordIdx < numCoord; coordIdx++) {
            grid[yCoords[coordIdx]][xCoords[coordIdx]] += 1;
        }      
    }
});

counter = 0;
for (let i = 0; i < 1000; i++) {
    for (let j = 0; j < 1000; j++) {
        if (grid[i][j] > 1) {
            counter++;
        }
    }
}

console.log(counter);


