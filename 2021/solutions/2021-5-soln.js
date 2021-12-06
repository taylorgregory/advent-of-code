const fs = require('fs');
array = fs.readFileSync('../inputs/2021-5-input.txt', 'utf8').split('\r\n'); 

console.log(array);
array.forEach((coordinate, coordinateIdx) => {
    firstCoord = coordinate.split(' -> ')[0];
    secondCoord = coordinate.split(' -> ')[1];
    array[coordinateIdx] = [firstCoord.split(',')[0], firstCoord.split(',')[1], secondCoord.split(',')[0], secondCoord.split(',')[1]].map(Number);

});

// Filtering out the coordinates that do not form horizontal or vertical lines
array = array.filter((coordinate) => {
    return (coordinate[0] == coordinate[2]) || (coordinate[1] == coordinate[3])
});

// Initialise an empty 1000 X 1000 array

/* array.forEach((coordinate) => {
    
}); */







// initialise an empty 1000 x 1000 array

