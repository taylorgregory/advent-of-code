from textwrap import dedent
from aocd import get_data, submit
import math
import re

'''---------------------------------------------------------------------------------------------------------
PLOT SUMMARY:
* You reach a station containing gondola lifts that will take you to the water source
* The gondola lifts are not working, and an engineer Elf explains that the engine is missing a part
* It is unclear which part is missing, and so you use the engine schematic (puzzle input A) to work this out
---------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------------------------------------------------------------------
FORMAT_DATA() SUMMARY:
format_data() is a helper function to reformat the string input into an array of arrays, such that each
character is an element of the subarray.
---------------------------------------------------------------------------------------------------------'''
def format_data(input_str):
    return [[char for char in x] for x in input_str.splitlines()]

# input: non-numerical character
# output: a list of all surrounding numbers
# assumption: a single number doesn't touch two non-numerical characters    
def find_surrounding_numbers(input, row, col):
    all_nums = []
    for r in [row-1, row, row+1]:
        l_pos = max(col-1, 0)
        r_pos = min(col+1, len(input[row])-1)  

        while l_pos > 0 and input[r][l_pos].isnumeric() and input[r][l_pos-1].isnumeric(): l_pos -= 1
        while r_pos < len(input[row])-1 and input[r][r_pos].isnumeric() and input[r][r_pos+1].isnumeric(): r_pos += 1

        all_nums.extend([int(x) for x in ''.join(input[r][l_pos:r_pos+1]).replace(input[row][col], '.').split('.') if x])

    return all_nums

def part_a(input):
    total = 0
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if not char.isnumeric() and char != '.':
                total += sum(find_surrounding_numbers(input, i, j)) 
    return total

def part_b(input):
    total = 0
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == '*':
                surrounding_numbers = find_surrounding_numbers(input, i, j)
                if (len(surrounding_numbers) == 2):
                    total += math.prod(surrounding_numbers)
    return total

if __name__ == "__main__":
    # Test data
    test_string = dedent("""
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """).strip("\n")
    
    # Run tests for Part A and Part B
    test_data = format_data(test_string)
    assert part_a(test_data) == 4361
    assert part_b(test_data) == 467835

    # Submit answers for Part A and Part B
    data = format_data(get_data(day=3, year=2023))
    print(part_a(data))
    print(part_b(data))
    #submit(part_a(data), part="a", day=3, year=2023)    
    #submit(part_b(data), part="b", day=3, year=2023)