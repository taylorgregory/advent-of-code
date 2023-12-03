with open('Untitled2.txt') as file:
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
    
    red_max = 0
    green_max = 0
    blue_max = 0
    
    for j in range(len(game_data)):
        current_draw = game_data[j].split(' ')
        if current_draw[1] == 'red' and int(current_draw[0]) > red_max:
            red_max = int(current_draw[0])
        elif current_draw[1] == 'green' and int(current_draw[0]) > green_max:
            green_max = int(current_draw[0])
        elif current_draw[1] == 'blue' and int(current_draw[0]) > blue_max:
            blue_max = int(current_draw[0])
            
    power_total += red_max * green_max * blue_max
    
print(power_total)
