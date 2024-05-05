from textwrap import dedent
from aocd import get_data, submit
from math import prod

'''---------------------------------------------------------------------------------------------------------
PLOT SUMMARY:
* You have been launched into the atmosphere and land on Snow Island floating in the sky
* There is very little snow on Snow Island as snow production has stopped due to a lack of water
* You have to walk a while with an Elf, and so you play a game to fill the time
* Data from these games form your puzzle input
---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------
PART A RIDDLE SUMMARY:
For Part A, we are told that you have a bag containing only 12 red cubes, 13 green cubes, and 14 blue cubes. 
With this information, we need to look at the draws in each game and determine which of these games are
possible. The final result for this puzzle is to be the sum of all of the valid game IDs. For example:
[insert example].
---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------
PART B RIDDLE SUMMARY:
Part B takes the same puzzle input, however the question at hand is 'what is the fewest number of cubes of
each colour that could have been in the bag to make the game possible?'. Considering this, the 'power' of 
a single game is the product of the minimum possible number of red, green, and blue cubes. Then, the final 
result for this puzzle is obtained by taking the sum of all games' powers. 
---------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------------------------------------------------------------------
SOLUTION SET 1 SUMMARY:
I have had two main attempts at this challenge. The first attempt is one that came quite naturally to me
and makes use of for loops, booleans and a counter variable to produce my result.
---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------
FORMAT_DATA() SUMMARY:
This format data function takes input such as:

'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue...'

and returns input in an array such as:

[
    ['3 blue', '4 red', '1 red', '2 green', '6 blue', '2 green'],
    ['1 blue', '2 green', '3 green', '4 blue', '1 red', '1 green', '1 blue'],
    ...
]

Note that by reformatting the data in this way, we lose the following information:
* The game ID (e.g., 'Game 1:')
* Which colour/number pair belongs to each draw (i.e. the information obtained by the semi-colons in the
original data)

Removing this information forces assumptions about the data which will be outlined in each of the solutions
below.
---------------------------------------------------------------------------------------------------------'''
def format_data(input_str):
    return [game.split(": ")[1].replace(";", ",").split(", ") for game in input_str.splitlines()]

'''---------------------------------------------------------------------------------------------------------
PART_A() SUMMARY:
This approach to part A first starts with defining the known number of colours that exist within the bag. 
Next, a counter is initialised which will be iteratively updated to produce the final result. Specifically,
we iterate through the input array, and if any of the colours recorded is greater than the known values in 
the bag, then this draw is deemed invalid and we move onto looking at the next draw. Otherwise, if all
colours drawn are valid, then the game number is added to the total. 

Note that two major assumptions have been made here - both related to the way that the input data has been
formatted. 
* As outlined above, the game ID has not been retained, and so when I say that the game number is added to 
the total, I am making the assumption that all game IDs are in order and that the game's index within the
input array is equal to the Game ID - 1 (we minus 1 as indexing starts at 0 but the game ID starts at 1)
*[to rewrite] 
Further, information about each draw is not retained. With this, we make an assumption that the concept
of each draw within a game doesn't provide useful information, and that we just need to check each number/
colour pairing to understand the validity of each draw. It assumes that a single draw will never be written
as '3 red, 4 blue, 11 red', as the red values are only considered separately - and this would be considered
valid according to my solution even though the sum exceeds the maximum allowed red value of 12.
---------------------------------------------------------------------------------------------------------'''
def part_a(input):
    # Defining known values in bag
    colours_in_bag =  { "red": 12, "green": 13, "blue": 14 }

    total = 0
    for i, row in enumerate(input):
        valid_draw = True
        for draw in row:
            number, colour = draw.split(' ')
            # If any of the colours drawn exceeds the known amounts, then this game is deemed invalid
            if int(number) > colours_in_bag[colour]:
                valid_draw = False
                break

        # If a valid game, then we append this game ID to the total counter
        if valid_draw:
            total += i + 1

    return total


'''---------------------------------------------------------------------------------------------------------
This Part B solution is similar to the Part A solution above, however instead of recording the known maximum 
values for the bag, each row records the the maximum number of each colour. That is, we iterate through 
each of the games, and then each of the draws within that game. After all draws within a game is visited, 
then the max_cols dictionary will contain the maximum of each colour for that game. Then, the power is
calculated and added to the overall power total which is the final result.
---------------------------------------------------------------------------------------------------------'''
def part_b(input):
    power_total = 0
    for row in input:
        # Initialising the dictionary that stores the max of each colour for each game
        max_cols =  { "red": 0, "green": 0, "blue": 0 }

        # Iterate through each of this game's draws to determine the maximum of each colour
        for draw in row:
            this_number, this_colour = draw.split(' ')   
            if int(this_number) > max_cols[this_colour]:
                max_cols[this_colour] = int(this_number)

        # Calculate this game's power and add this to the overall power total
        power_total += max_cols['red'] * max_cols['green'] * max_cols['blue']
        
    return power_total

'''---------------------------------------------------------------------------------------------------------
SOLUTION SET 2 SUMMARY:
I quite like the solution above - it's simple and readable. However, much of this Advent of Code experience
is to push me to think outside the box, come up with different solutions, and challenge my normal way of 
thinking. As such, I've put together the following secondary set of solutions. Note that the data is
initially formatted in a different way (using dictionaries) and list comprehension is much more heavily 
utilised - sometimes unfortunately at the cost of readability. 
---------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------
FORMAT DATA SUMMARY:
format_data() is a helper function to reformat the data into lists of dictionaries. For example, it takes 
the following input:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

and returns the following output:

    [[{"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}], [{},{}]]

As the draws themselves are retained (through using separate dictionaries for each draw), then the only 
piece of information that is lost through this reformatting is the game ID.

---> Possible improvement: still remove the concept of draws as I don't actually think it's needed.
All other functions will need modification here too.
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

'''---------------------------------------------------------------------------------------------------------
GET_MAX_COLS() SUMMARY:
Unlike my previous approach, this approach uses an extra helper function: get_max_cols(). This helper
function is to be used within both parts, and takes a list of several dictionaries as input, and returns
one dictionary that gives the max of each colour for a given game.
---------------------------------------------------------------------------------------------------------'''
# Insert helper function to find max of each colour
# feed in a list of several dictionaries, return one resulting dictionary which gives the max
def get_max_cols(list):
    result = {}
    for dict in list:
        for key, value in dict.items():
            result[key] = max(result[key], value) if key in result else value

    return result    

'''---------------------------------------------------------------------------------------------------------
PART_A() SUMMARY:
Firstly, like my previous approach, we start by defining the known number of colours that exist within the 
bag. Then, the get_max_cols() function is utilised to reduce the list of dictionaries to a single dictionary
of only the max of each colour. Finally, the maximums are compared to the known values of the bag to
understand the validity of this draw.

I don't particularly like this final line of this function as I believe it to be quite unreadable, however
I was interested to see how I could this in a single line using an aggregate function, list comprehension, 
and an inline if statement.

--> If this was to be rewritten, the get_max_cols function is not overly necessary. However, it was
convenient to use here due to the structure of the data.
---------------------------------------------------------------------------------------------------------'''
def part_a(input):
    # Amount of each colour in the bag as defined by the Elf
    bag =  { "red": 12, "green": 13, "blue": 14 }
    max = [get_max_cols(game) for game in input]
    return sum([i+1 if all(game[key] <= bag[key] for key in bag.keys()) else 0 for i, game in enumerate(max)])

'''---------------------------------------------------------------------------------------------------------
PART_B() SUMMARY:
Writing this solution was very nice as it sees list comprehension and my helper function come together for
a relatively simple one line solution. That is, the result of the helper function just need to be multiplied
and then summed to produce the result.
---------------------------------------------------------------------------------------------------------'''
def part_b(input):
    return sum([prod(get_max_cols(game).values()) for game in input])

if __name__ == "__main__":
    # Testing
    test_string = dedent("""
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
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