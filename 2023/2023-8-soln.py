from aocd import get_data, submit

def format_data(input_str):
    input_arr = input_str.splitlines()
    instructions = input_arr[0]

    dict = {}
    for i in range(2, len(input_arr)):
        key, value = input_arr[i].split(" = ")
        dict[key] = value.replace("(", "").replace(",", "").replace(")", "").split(" ")

    return instructions, dict

def part_a(instructions, dict):
    lr_dict = {
        "L": 0,
        "R": 1
    }

    location = "AAA"
    mod_counter = 0
    num_moves = 0
    while location != "ZZZ":
        location = dict[location][lr_dict[instructions[mod_counter % len(instructions)]]]
        mod_counter += 1
        num_moves += 1

    return num_moves

def part_b(instructions, dict):
    return instructions, dict

if __name__ == "__main__":
    # Testing
    test_string_1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

    test_string_2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

    test_moves_1, test_dict_1 = format_data(test_string_1)
    assert part_a(test_moves_1, test_dict_1) == 2

    test_moves_2, test_dict_2 = format_data(test_string_2)
    assert part_a(test_moves_2, test_dict_2) == 6

    moves, dict = format_data(get_data(day=8, year=2023))
    submit(part_a(moves, dict), part="a", day=8, year=2023)  
