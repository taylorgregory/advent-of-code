import re

with open('../inputs/2023-1-input.txt') as file:
    input_arr = file.read().splitlines()

rolling_total = 0

for i in range(len(input_arr)):
    filtered_row = re.sub('\D', '', input_arr[i])
    rolling_total += int(filtered_row[0] + filtered_row[len(filtered_row) - 1])

print(rolling_total)

