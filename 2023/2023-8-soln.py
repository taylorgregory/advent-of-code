from aocd import get_data, submit
import re

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

    lr_dict = {
        "L": 0,
        "R": 1
    }
    # Get all instructions that end in A
    a_ending = {key: val for key, val in dict.items() if re.search(f"A$", key)}

    # Make result list that holds the locations for each 
    locations = list(a_ending.keys())
    mod_counter = 0
    num_moves = 0
    num_z = 0
    while num_z < len(locations):
        num_z = 0
        for i, location in enumerate(locations):
            locations[i] = dict[location][lr_dict[instructions[mod_counter % len(instructions)]]]
            if re.search(f"Z$", locations[i]):
                num_z += 1
        mod_counter += 1
        num_moves += 1
        print(num_moves)
        print(num_z)

    return num_moves

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

    test_string_3 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

    test_moves_1, test_dict_1 = format_data(test_string_1)
    assert part_a(test_moves_1, test_dict_1) == 2

    test_moves_2, test_dict_2 = format_data(test_string_2)
    assert part_a(test_moves_2, test_dict_2) == 6

    test_moves_3, test_dict_3 = format_data(test_string_3)
    print(part_b(test_moves_3, test_dict_3))

    moves, dict = format_data(get_data(day=8, year=2023))
    #submit(part_a(moves, dict), part="a", day=8, year=2023)  
    print(part_b(moves, dict))
