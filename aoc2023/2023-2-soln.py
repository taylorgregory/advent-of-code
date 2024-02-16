from aocd import get_data, submit

def part_a(input):
    colours_in_bag =  {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    id_total = 0
    for i, row in enumerate(input):
        game_data = row.split(': ')[1].replace(';', ',').split(', ')
        valid_draw = True

        for data in game_data:
            current_draw = data.split(' ')
            if int(current_draw[0]) > colours_in_bag[current_draw[1]]:
                valid_draw = False
                break
            
        if valid_draw:
            id_total += i + 1

    return id_total

def part_b(input):
    power_total = 0
    for row in input:
        game_data = row.split(': ')[1].replace(';', ',').split(', ')
        
        max_cols =  {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        
        for data in game_data:
            current_draw = data.split(' ')   
            if int(current_draw[0]) > max_cols[current_draw[1]]:
                max_cols[current_draw[1]] = int(current_draw[0])
                
        power_total += max_cols['red'] * max_cols['green'] * max_cols['blue']
        
    return power_total

if __name__ == "__main__":
    input_arr = get_data(day=2, year=2023).splitlines()

    # Part A
    part_a_answer = part_a(input_arr)
    print("Submitting " + str(part_a_answer) + " for Part A...")
    submit(part_a_answer, part="a", day=2, year=2023)
    
    # Part B
    part_b_answer = part_b(input_arr)
    print("Submitting " + str(part_b_answer) + " for Part B...")
    submit(part_b_answer, part="b", day=2, year=2023)