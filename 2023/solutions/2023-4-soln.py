import numpy

with open('../inputs/2023-4-input.txt') as file:
    input_arr = file.read().splitlines()

total_counter = 0
results = numpy.ones((len(input_arr), 2))
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

    # update num wins in arr
    results[i][0] = num_wins

    # update num cards
    for j in range(1, num_wins + 1):
        results[i+j][1] += results[i][1]


for result in results:
    part_b_total += int(result[1])

print(total_counter)
print(part_b_total)