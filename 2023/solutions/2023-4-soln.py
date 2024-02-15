with open('../inputs/2023-4-input.txt') as file:
    input_arr = file.read().splitlines()

total_counter = 0

for i in range(len(input_arr)):
    winning_numbers = input_arr[i].split(": ")[1].split(" | ")[0].replace("  ", " ").strip().split(" ")
    your_numbers = input_arr[i].split(": ")[1].split(" | ")[1].replace("  ", " ").strip().split(" ")

    counter = 0
    for your_number in your_numbers:
        if your_number in winning_numbers:
            counter = 1 if counter == 0 else counter * 2

    total_counter += counter

print(total_counter)