from aocd import get_data, submit
import math

def check_location(input, row, column):
    if input[row] and input[row][column].isnumeric():
        left_loc = column
        while left_loc > 0 and input[row][left_loc-1].isnumeric():
            left_loc -= 1
        
        right_loc = column
        while right_loc < len(input[row]) - 1 and input[row][right_loc+1].isnumeric():
            right_loc += 1

        number = ''
        for k in range(left_loc, right_loc+1):
            number += str(input[row][k])
            input[row][k] = '.'
        
        return int(number)
    else:
        return 0
    
def part_a(input):
    part_a_input = input
    total = 0
    for i, row in enumerate(part_a_input):
        for j, char in enumerate(row):
            # if it is a special character
            if not char.isnumeric() and char != '.':
                total += check_location(part_a_input, i-1, j-1)
                total += check_location(part_a_input, i-1, j)
                total += check_location(part_a_input, i-1, j+1)
                total += check_location(part_a_input, i, j-1)
                total += check_location(part_a_input, i, j+1)
                total += check_location(part_a_input, i+1, j-1)
                total += check_location(part_a_input, i+1, j)
                total += check_location(part_a_input, i+1, j+1)   
    return total

def part_b(input):
    part_b_input = input
    total = 0
    for i, row in enumerate(part_b_input):
        for j, char in enumerate(row):
            if char == '*':
                nearby_numbers = [1] * 8
                nearby_numbers[0] += check_location(part_b_input, i-1,j-1)
                nearby_numbers[1] += check_location(part_b_input, i-1,j)
                nearby_numbers[2] += check_location(part_b_input, i-1,j+1)
                nearby_numbers[3] += check_location(part_b_input, i,j-1)
                nearby_numbers[4] += check_location(part_b_input, i,j+1)
                nearby_numbers[5] += check_location(part_b_input, i+1,j-1)
                nearby_numbers[6] += check_location(part_b_input, i+1,j)
                nearby_numbers[7] += check_location(part_b_input, i+1,j+1)

                print(nearby_numbers)

                if sum(x != 0 for x in nearby_numbers) == 2:
                    total += math.prod(nearby_numbers)
    
    print(total)
    return total

if __name__ == "__main__":

    # Get all data
    test_data = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.splitlines()
    
    for i, row in enumerate(test_data):
        test_data[i] = [char for char in test_data[i]]

    data = get_data(day=3, year=2023).splitlines()
    
    for row in data:
        row = [char for char in row]

    # Run tests for Part A and Part B
    assert part_a(test_data) == 4361
    assert part_b(test_data) == 467835

    # Submit answers for Part A and Part B
    submit(part_a(data), part="a", day=3, year=2023)    
    submit(part_b(data), part="b", day=3, year=2023)