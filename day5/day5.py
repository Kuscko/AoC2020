# Advent of Code 2020 Day 5 - Binary Boarding

# F = lower half, B = upper half, L = lower half, R = upper half

with open('inputs/day_05-input.txt', 'r') as file:
    input = file.read().splitlines()

# Converts each line to binary string, then int([x],2) converts each line to equivalent decimal number
seats = [int(line.replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1"),2) for line in input]

# iterates from lowest value in seats to highest in seats.
# If the seat is not in seats, then assign it to the your_seat.
for seat in range(min(seats), max(seats)):
    if seat not in seats:
        your_seat = seat

# Part 1 Solution
# print the max value for all seats
print("Part 1 Solution: ", max(seats))

# Part 2 Solution
# print your seat if it isn't found in your seat list
print("Part 2 Solution: ", your_seat)