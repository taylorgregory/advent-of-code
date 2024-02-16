import numpy
from aocd import get_data

input_arr = get_data(day=4, year=2023).splitlines()

total_counter = 0
results = numpy.ones((len(input_arr), 1))
part_b_total = 0

for i in range(len(input_arr)):
    winning_numbers = input_arr[i].split(": ")[1].split(" | ")[0].replace("  ", " ").strip().split(" ")
    your_numbers = input_arr[i].split(": ")[1].split(" | ")[1].replace("  ", " ").strip().split(" ")

    # PART A START #
    counter = 0
    for your_number in your_numbers:
        if your_number in winning_numbers:
            counter = 1 if counter == 0 else counter * 2

    total_counter += counter
    # PART A END #

    # PART B START #
    num_wins = 0
    for your_number in your_numbers:
        if your_number in winning_numbers:
            num_wins += 1

    # update num cards
    for j in range(1, num_wins + 1):
        results[i+j] += results[i]


for result in results:
    part_b_total += int(result[0])
# END PART B #

print(total_counter)
print(part_b_total)