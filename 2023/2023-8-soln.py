from aocd import get_data, submit
import re
import numpy as np
from textwrap import dedent

# Data is imported 

def format_data(input_str):
    input_arr = input_str.splitlines()
    instructions = input_arr[0]

    dict = {}
    for i in range(2, len(input_arr)):
        key, value = input_arr[i].split(" = ")
        dict[key] = value.replace("(", "").replace(",", "").replace(")", "").split(" ")

    return instructions, dict

def part_a(instructions, dict):
    moves = ["AAA"]
    while moves[len(moves)-1] != "ZZZ":
        left_right = 0 if instructions[(len(moves)-1) % len(instructions)] == "L" else 1
        moves.append(dict[moves[len(moves)-1]][left_right])  
    return len(moves)-1

def part_b(instructions, dict):
    dedent("""\
    A one-line summary of the module or program, terminated by a period.

    Leave one blank line.  The rest of this docstring should contain an
    overall description of the module or program.  Optionally, it may also
    contain a brief description of exported classes and functions and/or usage
    examples.

    Typical usage example:

    foo = ClassFoo()
    bar = foo.FunctionBar()
    """)

    # Obtaining a list of all the A starting points
    a_ending = {key: val for key, val in dict.items() if re.search(f"A$", key)}
    locations = list(a_ending.keys())
    all_moves = []

    for location in locations:
        moves = [location]
        while not re.search(f"Z$", moves[len(moves)-1]):
            left_right = 0 if instructions[(len(moves)-1) % len(instructions)] == "L" else 1
            moves.append(dict[moves[len(moves)-1]][left_right])  
        all_moves.append(moves)

    return np.lcm.reduce([len(x)-1 for x in all_moves])



if __name__ == "__main__":

    print(part_b.__doc__)
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
    assert part_b(test_moves_3, test_dict_3) == 6

    moves, dict = format_data(get_data(day=8, year=2023))
    submit(part_a(moves, dict), part="a", day=8, year=2023)  
    submit(part_b(moves, dict), part="b", day=8, year=2023) 