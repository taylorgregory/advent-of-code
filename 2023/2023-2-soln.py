from textwrap import dedent
from aocd import get_data, submit
from math import prod

'''---------------------------------------------------------------------------------------------------------
PLOT SUMMARY:
* INSERT SUMMARY
* Data from these games form your puzzle input
---------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------------------------------------------------------------------
FORMAT DATA SUMMARY:
format_data() is a helper function to reformat the data into lists of dictionaries. For example, it takes 
the following input:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

and returns the following output:

    [[{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}], [{},{}]]

---------------------------------------------------------------------------------------------------------'''
def format_data(input_str):
    # First, split into a list-type structure
    reformatted_input = [[y.split(", ") for y in x.split(": ")[1].split("; ")] for x in input_str.splitlines()]

    # Convert the list of lists to list of dictionaries by zipping the two lists
    for i, game in enumerate(reformatted_input):
        for j, draw in enumerate(game):
            num_list = [int(num_col.split(" ")[0]) for num_col in draw]
            col_list = [num_col.split(" ")[1] for num_col in draw]
            reformatted_input[i][j] = dict(zip(col_list, num_list))

    return reformatted_input

# Insert helper function to find max of each colour
# feed in a list of several dictionaries, return one resulting dictionary which gives the max
def get_max_cols(list):
    result = {}
    for dict in list:
        for key, value in dict.items():
            result[key] = max(result[key], value) if key in result else value

    return result    

def part_a(input):
    # Amount of each colour in the bag as defined by the Elf
    bag =  { "red": 12, "green": 13, "blue": 14 }
    max = [get_max_cols(game) for game in input]
    return sum([i+1 if all(game[key] <= bag[key] for key in bag.keys()) else 0 for i, game in enumerate(max)])

def part_b(input):
    return sum([prod(get_max_cols(game).values()) for game in input])

if __name__ == "__main__":
    # Testing
    test_string = dedent("""
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 vblue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """).strip("\n")
    
    test_data = format_data(test_string)
    assert part_a(test_data) == 8
    assert part_b(test_data) == 2286

    # Submission
    data = format_data(get_data(day=2, year=2023))
    submit(part_a(data), part="a", day=2, year=2023)    
    submit(part_b(data), part="b", day=2, year=2023)