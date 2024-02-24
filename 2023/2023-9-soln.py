from aocd import get_data, submit
from collections import Counter

def format_data(input_str):
    return [[int(y) for y in x.split(" ")] for x in input_str.splitlines()]

def part_a(input):
    sum = 0
    for history in input:
        diff_arr = [history]
        diff_counter = 0
        while Counter(diff_arr[diff_counter])[0] != len(diff_arr[diff_counter]):
            diff_counter += 1
            this_diff = []
            for i in range(1, len(diff_arr[diff_counter-1])):
                this_diff.append(diff_arr[diff_counter-1][i] - diff_arr[diff_counter-1][i-1])
            diff_arr.append(this_diff)
    
        for i in reversed(range(len(diff_arr)-1)):
            num_to_append = diff_arr[i][len(diff_arr[i])-1] + (diff_arr[i+1][len(diff_arr[i+1])-1])
            diff_arr[i].append(num_to_append)
        
        sum += diff_arr[0][len(diff_arr[0])-1]

    return sum

if __name__ == "__main__":
    # Testing
    test_string = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

    test_arr = format_data(test_string)
    assert part_a(test_arr) == 114

    data = format_data(get_data(day=9, year=2023))
    submit(part_a(data), part="a", day=9, year=2023) 