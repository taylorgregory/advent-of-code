with open('../inputs/2023-4-input.txt') as file:
    input_arr = file.read().splitlines()

total_counter = 0

for i in range(len(input_arr)):
    winning_numbers = input_arr[i].split(": ")[1].split(" | ")[0].replace("  ", " ").strip()
    your_numbers = input_arr[i].split(": ")[1].split(" | ")[1].replace("  ", " ").strip()
    winning_numbers_arr = winning_numbers.split(" ")
    your_numbers_arr = your_numbers.split(" ")

    counter = 0
    for your_number in your_numbers_arr:
        if your_number in winning_numbers_arr:
            if counter == 0:
                counter = 1
            else:
                counter = counter * 2

    total_counter += counter

print(total_counter)