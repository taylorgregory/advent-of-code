import re
from aocd import get_data, submit

def part_a(input):
    rolling_total = 0
    for row in input:
        filtered_row = re.sub('\D', '', row)
        first_num = filtered_row[0]
        last_num = filtered_row[len(filtered_row) - 1]
        rolling_total += int(first_num + last_num)

    return rolling_total

def part_b(input):
    rolling_total = 0
    for row in input:
        # HATE this (but works for now)..TBC:
        words_to_nums = {'one': 'one1one', 'two': 'two2two', 'three': 'three3three', 'four': 'four4four', 'five': 'five5five', 'six': 'six6six', 'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'}
        for key, value in words_to_nums.items():
            row = row.replace(key, value)

        filtered_row = re.sub('\D', '', row)
        first_num = filtered_row[0]
        last_num = filtered_row[len(filtered_row) - 1]
        rolling_total += int(first_num + last_num)

    return rolling_total

if __name__ == "__main__":
    test_data_a = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''.splitlines()
    
    test_data_b = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.splitlines()
    
    data = get_data(day=1, year=2023).splitlines()
    
    # Run tests for Part A and Part B
    assert part_a(test_data_a) == 142
    assert part_b(test_data_b) == 281

    # Submit answers for Part A and Part B
    submit(part_a(data), part="a", day=1, year=2023)    
    submit(part_b(data), part="b", day=1, year=2023)