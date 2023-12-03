with open('../inputs/2023-2-input.txt') as file:
    input_arr = file.read().splitlines()

colours_in_bag =  {
    "red": 12,
    "green": 13,
    "blue": 14
}

id_total = 0

for i in range(len(input_arr)):
    game_data = input_arr[i].split(': ')[1].replace(';', ',').split(', ')
    valid_draw = True

    for j in range(len(game_data)):
        current_draw = game_data[j].split(' ')
        if int(current_draw[0]) > colours_in_bag[current_draw[1]]:
            valid_draw = False
            break
        
    if valid_draw == True:
        id_total += i + 1

print(id_total)
