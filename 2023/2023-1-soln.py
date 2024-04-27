import re
from aocd import get_data, submit
from words2num import w2n

'''---------------------------------------------------------------------------------------------------------
PLOT SUMMARY:
* There's a problem with global snow production and you're tasked with taking a look.
* You're being strapped into a trebuchet to go to the sky (this is where snow comes from after all!)
* There is a problem with the elves' calibration document, which is the puzzle input. You need to fix it!
* Q: What was the calibration document for? Your travel locations?
---------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------------------------------------------------------------------
PART A SUMMARY:
Part A was a fairly friendly puzzle to kick off the 2023 AoC. For each string provided, you need to
determine the first and last digit, concatenate these to make a new number, and then return the sum of all
of these. For example, [insert example].

To approach this, I have used list comprehension to remove all non-digits from each string.
Then, list comprehension has been used again to concatenate the first and last digits into a new list. This 
list is summed across to provide the final answer. 

Check out my code:
---------------------------------------------------------------------------------------------------------'''
def part_a(input):
    # Filter the rows such that they only contain digits
    filtered_rows = [re.sub('\D', '', x) for x in input.splitlines()]

    # Concatenate the first digit and final digit in each row, and then sum across all rows
    return sum([int(x[0] + x[len(x)-1]) for x in filtered_rows])

'''---------------------------------------------------------------------------------------------------------
PART B SUMMARY:
Part B threw a little more of a curveball than Part A. In this riddle, the same puzzle input is used with 
the same final goal, however this time digits written in English are to be considered too. For example, 
[insert example].

I started this out with a naive approach, namely, just find and replace all written digits with their 
corresponding value. However, as should be expected from AoC, this didn't quite cut it. Consider input such
as the following: [walk through the following input: 723one234nineight]

Next, instead of doing a 'find and replace' solution, I implemented a 'find and insert' approach. That is, 
I used regular expressions to find all matches in a given row. In the example above, a search on 
723one234nineight would return matches for 'one', 'nine' and 'eight'. Then, we loop through each of the
matches, and insert the corresponding digit at the *start* of the written digit. Finally, as all of the 
necessary digits are now in the string, code identical to that used in Part A can be used to discard the
non-numeric values and return the required answer. 

Check out my code:
---------------------------------------------------------------------------------------------------------'''
def part_b(input):
    updated_rows = []
    for row in input.splitlines():
        # As strings are immutable in python, we had to work with a list instead of a string
        row_arr = [*row]
        matches = re.finditer(f'(?=({"one|two|three|four|five|six|seven|eight|nine"}))', row)
        for i, match in enumerate(matches):
            # +i is required as it will account for the number of matches that have already been inserted
            row_arr.insert(match.start()+i, str(w2n(match.group(1))))

        # Join the 'working' list to be in the original form 
        updated_rows.append("".join(row_arr))

    # Like Part A, filter the rows to only contain digits, concatenate first and last digits, and then sum
    filtered_rows = [re.sub('\D', '', row) for row in updated_rows]
    return sum([int(row[0] + row[len(row)-1]) for row in filtered_rows])

if __name__ == "__main__":
    # Get all data
    test_data_a = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
    
    test_data_b = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
    
    data = get_data(day=1, year=2023)
    
    # Run tests for Part A and Part B
    assert part_a(test_data_a) == 142
    assert part_b(test_data_b) == 281

    # Submit answers for Part A and Part B
    submit(part_a(data), part="a", day=1, year=2023)    
    submit(part_b(data), part="b", day=1, year=2023)