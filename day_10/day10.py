# Advent of Code 2020 Day 10 - Adapter Array

class Solutions:
    def __init__(self, adapters):
        self.adapters = adapters
    
    def find_solution_pt1(self):
        ''' 
            Find the number of jolt differences, 1 & 3. Multiply them together then return result.

            Args:
                Self -> int list of adapters
        '''
        difference_of_one = 0
        difference_of_two = 0
        difference_of_three = 1

        for x in adapters:
            differences = x - current_value
            current_value = x
            if differences <= 3 and differences >= 1:
                if differences == 1: 
                    difference_of_one += 1
                elif differences == 2: 
                    difference_of_two += 1
                else: 
                    difference_of_three += 1
        return difference_of_one * difference_of_three


with open('inputs/day_10-input.txt', 'r') as input:
    adapters = [int(input) for input in input.read().splitlines()]
    solution1 = Solutions.find_solution_pt1(adapters.sort())
    print(solution1)