import numpy as np
# reading the input lines from the given input file
with open('2021-1-input.txt') as inputval:
    lines = inputval.read().split('\n')

array = np.array([int(line) for line in lines])

# solution 1:
counter = 0
for idx, val in enumerate(array):
    if (idx < len(array) - 1):
        if (array[idx + 1] > array[idx]):
            counter = counter + 1

print(counter)

############################

# solution 2:
# aim: have two arrays (arr1 and arr2)
# trim the first element of arr1 and the last element of arr2
# arr1 - arr2
# if positive number, let value = 1, else, value = 0

# 1
# 2 1
# 3 2
# 4 3
#   4

# converting array of strings to array of numbers
arr1 = np.delete(array, 0)
arr2 = np.delete(array, len(array) - 1)

diff_arr = arr1 - arr2

bool_diff_arr = np.zeros(len(diff_arr))

for idx, val in enumerate(diff_arr):
    if val > 0:
        bool_diff_arr[idx] = 1

print(sum(bool_diff_arr))

##########################################
# PART 2: three sum sliding window

