# Advent of Code: Day 1 - Part 2
# completed by Patrick Kelly 5/30/2021 | 1:10AM

import os

# solution variables
goal = 2020
final_value = 0
solutions = []

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# open and loop through each value in the file
with open(file_path, 'r') as file:
    # assign each value in input file to list
    data = file.read().splitlines()
    for first in data:
        first_number = int(first)
        for second in data:
            second_number = int(second)
            for third in data:
                third_number = int(third)
                if (first_number + second_number + third_number) == goal:
                    # Prevents duplicates of values in the solutions list
                    if third_number in solutions:
                        break
                    solutions.append(first_number)
                    solutions.append(second_number)
                    solutions.append(third_number)
                    final_value = first_number * second_number * third_number

print("First Value: ", solutions[0])
print("Second Value: ", solutions[1])
print("Third Value: ", solutions[2])
print("Final Value: ", final_value)