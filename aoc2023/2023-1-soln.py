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
    input_arr = get_data(day=1, year=2023).splitlines()

    # Part A
    part_a_answer = part_a(input_arr)
    print("Submitting " + str(part_a_answer) + " for Part A...")
    submit(part_a_answer, part="a", day=1, year=2023)
    
    # Part B
    part_b_answer = part_b(input_arr)
    print("Submitting " + str(part_b_answer) + " for Part B...")
    submit(part_b_answer, part="b", day=1, year=2023)