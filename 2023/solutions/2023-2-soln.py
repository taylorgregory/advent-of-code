with open('../inputs/2023-2-input.txt') as file:
    input_arr = file.read().splitlines()

# PART A
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

# PART B
power_total = 0

for i in range(len(input_arr)):
    game_data = input_arr[i].split(': ')[1].replace(';', ',').split(', ')
    
    max_cols =  {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    
    for j in range(len(game_data)):
        current_draw = game_data[j].split(' ')   
        if int(current_draw[0]) > max_cols[current_draw[1]]:
            max_cols[current_draw[1]] = int(current_draw[0])
            
    power_total += max_cols['red'] * max_cols['green'] * max_cols['blue']
    
print(power_total)
