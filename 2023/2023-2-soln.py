from aocd import get_data, submit

def format_data(input_str):
    data = []
    for row in input_str.splitlines():
        data.append(row.split(': ')[1].replace(';', ',').split(', '))
    return data


def part_a(input):
    colours_in_bag =  {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total = 0
    for i, row in enumerate(input):
        valid_draw = True
        for draw in row:
            number, colour = draw.split(' ')
            if int(number) > colours_in_bag[colour]:
                valid_draw = False
                break
            
        if valid_draw:
            total += i + 1

    return total

def part_b(input):
    power_total = 0
    for row in input:
        max_cols =  {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for draw in row:
            this_number, this_colour = draw.split(' ')   
            if int(this_number) > max_cols[this_colour]:
                max_cols[this_colour] = int(this_number)
                
        power_total += max_cols['red'] * max_cols['green'] * max_cols['blue']
        
    return power_total

if __name__ == "__main__":
    # Testing
    test_string = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    
    test_data = format_data(test_string)
    assert part_a(test_data) == 8
    assert part_b(test_data) == 2286

    # Solve
    data = format_data(get_data(day=2, year=2023))
    submit(part_a(data), part="a", day=2, year=2023)    
    submit(part_b(data), part="b", day=2, year=2023)