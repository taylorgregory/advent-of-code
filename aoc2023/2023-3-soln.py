from aocd import get_data

input_arr = get_data(day=3, year=2023).splitlines()

for i in range(len(input_arr)):
    input_arr[i] = [char for char in input_arr[i]]

# PART A
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
        
        return int(number)
    else:
        return 0

total = 0

""" for i in range(len(input_arr)):
    for j in range(len(input_arr[i])):
        # if it is a special character
        if not input_arr[i][j].isnumeric() and input_arr[i][j] != '.':
            total += check_location(i-1, j-1)
            total += check_location(i-1, j)
            total += check_location(i-1, j+1)
            total += check_location(i, j-1)
            total += check_location(i, j+1)
            total += check_location(i+1, j-1)
            total += check_location(i+1, j)
            total += check_location(i+1, j+1)      """      

#print(total)

# PART B
b_total = 0

for i in range(len(input_arr)):
    for j in range(len(input_arr[i])):
        if input_arr[i][j] == '*':
            
            num_part_numbers = 0
            product = 1

            top_left = check_location(i-1,j-1)
            if (top_left > 0):
                product = product * top_left
                num_part_numbers += 1

            top = check_location(i-1,j)
            if (top > 0):
                product = product * top 
                num_part_numbers += 1

            top_right = check_location(i-1,j+1)
            if (top_right > 0):
                product = product * top_right
                num_part_numbers += 1

            left = check_location(i,j-1)
            if (left > 0):
                product = product * left
                num_part_numbers += 1

            right = check_location(i,j+1)
            if (right > 0):
                product = product * right
                num_part_numbers += 1

            bottom_left = check_location(i+1,j-1)
            if (bottom_left > 0):
                product = product * bottom_left
                num_part_numbers += 1

            bottom = check_location(i+1,j)
            if (bottom > 0):
                product = product * bottom
                num_part_numbers += 1

            bottom_right = check_location(i+1,j+1)
            if (bottom_right > 0):
                product = product * bottom_right
                num_part_numbers += 1

            if num_part_numbers == 2:
                b_total += product

print(b_total)
