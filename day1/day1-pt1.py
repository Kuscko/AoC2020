# Advent of Code: Day 1 - Part 1
# completed by Patrick Kelly 5/30/2021 | 12:27AM f

# solution variables
goal = 2020
final_value = 0
solutions = []

# open and loop through each value in the file
with open('P:\Portfolio\AoC2020\day1\input.txt', 'r') as file:
    # assign each value in input file to list
    data = file.read().splitlines()
    for first in data:
        first_number = int(first)
        for second in data:
            second_number = int(second)
            if first_number + second_number == goal:
                # Prevents duplicates of values in the solutions list
                if second_number in solutions:
                    break
                solutions.append(first_number)
                solutions.append(second_number)
                final_value = first_number * second_number

print("First Value: ", solutions[0])
print("Second Value: ", solutions[1])
print("Final Value: ", final_value)