import re

with open('../inputs/2023-1-input.txt') as file:
    input_arr = file.read().splitlines()

rolling_total = 0

for i in range(len(input_arr)):
    filtered_row = re.sub('\D', '', input_arr[i])
    first_num = filtered_row[0]
    last_num = filtered_row[len(filtered_row) - 1]
    rolling_total += int(first_num + last_num)

print(rolling_total)

