# Advent of Code: Day 2 - Part 1
# completed by Patrick Kelly 6/2/2021 | 6:57PM

import os

# define file path for the input file
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

valid_solutions = 0

# Opens the input file
with open(file_path) as f:
    # filters each line inside input file
    for line in f:
        # declare min, max, char, and pw variables
        nums, char, pw = line.split(" ")

        # use map to loop through the nums
        # variable and declare min/max values.
        min, max = map(int, nums.split("-"))
        char = char.split(":")[0]
        
        # if location in password has either character in 
        # location min or max, then add to counter.
        if((pw[min-1] == char) ^ (pw[max-1] == char)):
            valid_solutions += 1
        
print(valid_solutions)


