with open('../inputs/2023-2-input.txt') as file:
    input_arr = file.read().splitlines()

id_total = 0

for i in range(len(input_arr)):
    valid_draws = 0
    # Assumes that a single draw doesn't have two records for a single colour
    game_data = input_arr[i].split(': ')[1].replace(';', ',').split(', ')

    for j in range(len(game_data)):
        current_draw = game_data[j].split(' ')
        # Should use mapping here
        # Should also break if invalid draw exists
        if (current_draw[1] == 'red' and int(current_draw[0]) <= 12) or (current_draw[1] == 'green' and int(current_draw[0]) <= 13) or (current_draw[1] == 'blue' and int(current_draw[0]) <= 14):
            valid_draws += 1
    
    if valid_draws == len(game_data):
        id_total += i + 1

print(id_total)
    




