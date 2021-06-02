# Advent of Code: Day 2 - Part 1
# completed by Patrick Kelly 6/2/2021 | 6:24PM

import os

# get file path of input.txt
file_path = os.path.join(os.path.dirname(__file__),'input.txt')

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
        
        # if the number of characters in the password are between the min and max
        # values then the the solution is valid and should increment.
        if(max >= pw.count(char) >= min):
            valid_solutions += 1
        
print(valid_solutions)
