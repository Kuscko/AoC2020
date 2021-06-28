# Advent of Code 2020 Day 1 - Report Repair

# solution variables
goal = 2020
final_value = 0
solutions = []


# Advent of Code 2020 Day 1 - Part 1
def part_one():
# open and loop through each value in the file
    with open('inputs/day_01-input.txt', 'r') as file:
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


# Advent of Code 2020 Day 1 - Part 2
def part_two():
    # open and loop through each value in the file
    with open('inputs/day_01-input.txt', 'r') as file:
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
    print('-' * 25)
    print("First Value: ", solutions[0])
    print("Second Value: ", solutions[1])
    print("Third Value: ", solutions[2])
    print("Final Value: ", final_value)

part_one()
part_two()
