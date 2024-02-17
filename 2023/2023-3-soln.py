from aocd import get_data, submit

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
    total = 0

    for i, row in enumerate(input):
        for j, char in enumerate(row):
            # if it is a special character
            if not char.isnumeric() and char != '.':
                total += check_location(input, i-1, j-1)
                total += check_location(input, i-1, j)
                total += check_location(input, i-1, j+1)
                total += check_location(input, i, j-1)
                total += check_location(input, i, j+1)
                total += check_location(input, i+1, j-1)
                total += check_location(input, i+1, j)
                total += check_location(input, i+1, j+1)   

    return total

def part_b(input):
    total = 0

    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == '*':
                
                num_part_numbers = 0
                product = 1

                top_left = check_location(input, i-1,j-1)
                if (top_left > 0):
                    product = product * top_left
                    num_part_numbers += 1

                top = check_location(input, i-1,j)
                if (top > 0):
                    product = product * top 
                    num_part_numbers += 1

                top_right = check_location(input, i-1,j+1)
                if (top_right > 0):
                    product = product * top_right
                    num_part_numbers += 1

                left = check_location(input, i,j-1)
                if (left > 0):
                    product = product * left
                    num_part_numbers += 1

                right = check_location(input, i,j+1)
                if (right > 0):
                    product = product * right
                    num_part_numbers += 1

                bottom_left = check_location(input, i+1,j-1)
                if (bottom_left > 0):
                    product = product * bottom_left
                    num_part_numbers += 1

                bottom = check_location(input, i+1,j)
                if (bottom > 0):
                    product = product * bottom
                    num_part_numbers += 1

                bottom_right = check_location(input, i+1,j+1)
                if (bottom_right > 0):
                    product = product * bottom_right
                    num_part_numbers += 1

                if num_part_numbers == 2:
                    total += product

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
    assert part_a(test_data) == 8
    #assert part_b(test_data) == 2286

    # Submit answers for Part A and Part B
    submit(part_a(data), part="a", day=2, year=2023)    
    submit(part_b(data), part="b", day=2, year=2023)