import re
from aocd import get_data, submit
from words2num import w2n

def part_a(input):
    filtered_rows = [re.sub('\D', '', x) for x in input.splitlines()]
    return sum([int(x[0] + x[len(x)-1]) for x in filtered_rows])

def part_b(input):
    updated_rows = []
    for row in input.splitlines():
        row_arr = [*row]
        matches = re.finditer(f'(?=({"one|two|three|four|five|six|seven|eight|nine"}))', row)
        for i, match in enumerate(matches):
            row_arr.insert(match.start()+i, str(w2n(match.group(1))))
        updated_rows.append("".join(row_arr))

    filtered_rows = [re.sub('\D', '', row) for row in updated_rows]
    return sum([int(row[0] + row[len(row)-1]) for row in filtered_rows])

if __name__ == "__main__":
    # Get all data
    test_data_a = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
    
    test_data_b = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
    
    data = get_data(day=1, year=2023)
    
    # Run tests for Part A and Part B
    assert part_a(test_data_a) == 142
    assert part_b(test_data_b) == 281

    # Submit answers for Part A and Part B
    submit(part_a(data), part="a", day=1, year=2023)    
    submit(part_b(data), part="b", day=1, year=2023)