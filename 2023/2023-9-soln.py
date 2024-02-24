from aocd import get_data, submit
from collections import Counter

def format_data(input_str):
    return [[int(y) for y in x.split(" ")] for x in input_str.splitlines()]

def calculate_history(sequence):
    full_history = [sequence]
    diff_counter = 0
    while Counter(full_history[diff_counter])[0] != len(full_history[diff_counter]):
        diff_counter += 1
        this_diff = []
        for i in range(1, len(full_history[diff_counter-1])):
            this_diff.append(full_history[diff_counter-1][i] - full_history[diff_counter-1][i-1])
        full_history.append(this_diff)
    return full_history

def part_a(input):
    sum = 0
    for sequence in input:
        history = calculate_history(sequence)
        for i in reversed(range(len(history)-1)):
            num_to_append = history[i][len(history[i])-1] + (history[i+1][len(history[i+1])-1])
            history[i].append(num_to_append)      
        sum += history[0][len(history[0])-1]
    return sum

def part_b(input):
    sum = 0
    for sequence in input:
        history = calculate_history(sequence)    
        for i in reversed(range(len(history)-1)):
            num_to_append = history[i][0] - (history[i+1][0])
            history[i].insert(0, num_to_append)
        sum += history[0][0]
    return sum

if __name__ == "__main__":
    # Testing
    test_string = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

    test_arr = format_data(test_string)
    assert part_a(test_arr) == 114
    assert part_b(test_arr) == 2

    data = format_data(get_data(day=9, year=2023))
    submit(part_a(data), part="a", day=9, year=2023) 
    submit(part_b(data), part="b", day=9, year=2023) 