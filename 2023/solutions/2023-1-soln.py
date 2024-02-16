import re
from aocd import get_data

input_arr = get_data(day=1, year=2023).splitlines()

rolling_total = 0

for i in range(len(input_arr)):

    # TOGGLE COMMENT FOR PART A
    #filtered_row = re.sub('\D', '', input_arr[i])
    # END PART A

    # TOGGLE COMMENT FOR PART B
    this_row = input_arr[i]
    # HATE this (but works for now).......... TBC:
    words_to_nums = {'one': 'one1one', 'two': 'two2two', 'three': 'three3three', 'four': 'four4four', 'five': 'five5five', 'six': 'six6six', 'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'}
    for key, value in words_to_nums.items():
        this_row = this_row.replace(key, value)
    filtered_row = re.sub('\D', '', this_row)
    # END PART B

    first_num = filtered_row[0]
    last_num = filtered_row[len(filtered_row) - 1]
    rolling_total += int(first_num + last_num)

print(rolling_total)

