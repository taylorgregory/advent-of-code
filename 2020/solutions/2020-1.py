# reading the input lines from the given input file
with open('day1input.txt') as inputval:
    lines = inputval.read().split('\n')

# converting array of strings to array of numbers
int_array = [int(line) for line in lines]
sorted_array = sorted(int_array)

target_total = 2020

# PART 1: find two numbers that sum to target_total

# initial solution - brute force with efficiency order n^2
break_flag = False
for i in int_array:
    for j in int_array:
        if (i + j == target_total):
            val1 = i
            val2 = j
            break_flag = True
            break
    if (break_flag):
        break

print(val1)
print(val2)
print(val1 * val2)

# double pointer method
# get two variables: the lowerbound and the upper bound
lower_bound = 0
upper_bound = len(sorted_array) - 1

while (lower_bound < upper_bound):
    sum = sorted_array[lower_bound] + sorted_array[upper_bound]
    if (sum > target_total):
        upper_bound = upper_bound - 1
    elif (sum < target_total):
        lower_bound = lower_bound + 1
    elif (sum == target_total):
        val1 = sorted_array[lower_bound]
        val2 = sorted_array[upper_bound]
        break

print(val1)
print(val2)
print(val1 * val2)

# todo: hashing

# todo: break into functions


# PART 2: find three numbers that sum to target_total




