# Advent of Code: Day 2 - Part 1
# completed by Patrick Kelly 6/2/2021 | 6:24PM

valid_solutions_pt1 = 0
valid_solutions_pt2 = 0

# Opens the input file
with open('inputs/day_02-input.txt') as f:
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
            valid_solutions_pt1 += 1

        # if location in password has either character in 
        # location min or max, then add to counter.
        if((pw[min-1] == char) ^ (pw[max-1] == char)):
            valid_solutions_pt2 += 1
        
print('Part 1: ', valid_solutions_pt1)
print('Part 2: ', valid_solutions_pt2)
