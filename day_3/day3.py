# Advent of Code 2020 Day 3 - Toboggan Trajectory
import math

def create_list(file_name):
    """
        args: 
            file_name -> the file path to the input.txt file

        Returns: 
            Each line of the input txt file to a list as seperate values.
    """
    with(open(file_name) as f):
        return f.read().splitlines()

# fetch file path & create list
input_data = create_list('inputs/day_03-input.txt')

# declare constants
line_len = len(input_data[0])
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

# declare variables for counter
x_cordinate = 0
tree_count = []

"""

    Here I made sure to loop through each slope value (x_cordinate, y_cordinate)
    and determine if the character found at the input_data[y_cordinate][x_cordinate]
    equals "#". If true it increments the counter, changes the x_cordinate and continues.

    Once the for loop for the range finishes it selects the next slope, and repeat.

"""
for slope in slopes:
    counter = 0
    for y_cordinate in range(0, len(input_data), slope[1]):
        character = input_data[y_cordinate][x_cordinate]
        if character == "#":
            counter += 1
        x_cordinate = (x_cordinate + slope[0]) % line_len
    tree_count.append(counter)
    x_cordinate = 0 # set the x_cordinate to 0 so that it resets with each new slope in slopes.

print("Solution 1: ", tree_count[1])
print("Solution 2: ", math.prod(tree_count))
