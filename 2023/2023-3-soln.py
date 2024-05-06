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
    lbound = max(col-1, 0)
    rbound = min(col+1, len(input[row])-1)      
    ranges = [(row-1, lbound, rbound), (row, lbound, lbound), (row, rbound, rbound), (row+1, lbound, rbound)]

    all_nums = []
    for r, left_pos, right_pos in ranges:
        while left_pos > 0 and input[r][left_pos].isnumeric() and input[r][left_pos-1].isnumeric():
            left_pos -= 1
        
        while right_pos < len(input[row])-1 and input[r][right_pos].isnumeric() and input[r][right_pos+1].isnumeric():
            right_pos += 1

        unfiltered_list = ''.join(input[r][left_pos:right_pos+1]).split('.')
        all_nums.extend([int(x) for x in unfiltered_list if x])

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

    # Get all data
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
    submit(part_a(data), part="a", day=3, year=2023)    
    submit(part_b(data), part="b", day=3, year=2023)