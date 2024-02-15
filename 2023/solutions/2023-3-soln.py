import re

with open('../inputs/2023-3-input.txt') as file:
    input_arr = file.read().splitlines()

for i in range(len(input_arr)):
    input_arr[i] = [char for char in input_arr[i]]

def check_location(row, column):
    if input_arr[row] and input_arr[row][column].isnumeric():
        left_loc = column
        while left_loc > 0 and input_arr[row][left_loc-1].isnumeric():
            left_loc -= 1
        
        right_loc = column
        while right_loc < len(input_arr[row]) - 1 and input_arr[row][right_loc+1].isnumeric():
            right_loc += 1

        number = ''
        for k in range(left_loc, right_loc+1):
            number += str(input_arr[row][k])
            input_arr[row][k] = '.'
        
        return number
    else:
        return 0

total = 0

for i in range(len(input_arr)):
    for j in range(len(input_arr[i])):
        # if it is a special character
        if not input_arr[i][j].isnumeric() and input_arr[i][j] != '.':
            total += int(check_location(i-1, j-1))
            total += int(check_location(i-1, j))
            total += int(check_location(i-1, j+1))
            total += int(check_location(i, j-1))
            total += int(check_location(i, j+1))
            total += int(check_location(i+1, j-1))
            total += int(check_location(i+1, j))
            total += int(check_location(i+1, j+1))            

print(total)