# Advent of Code 2020 Day 9 - Encoding Error

class Solution:
    def __init__(self, input):
        self.input = input
    
    def find_solution_pt1(self, start, preamble, index):
        '''
            Loop through sets of 25 integers to find the first number that does have a sum of two seperate integers within the set of 25 integers.

            Args:
                self -> xmas_encryption list of integers
                start -> 0: beginning of xmas_encryption list, to me incremented. 
                preamble -> 25: end of preamble list, to me incremented and tested.
                index -> 25: index of number list in xmas_encryption, returned as answer.
        '''

        while index < len(self) - 1: # Prevent out of range exception
            number_list = self[start:preamble] # declare number list from [start:to:preamble]
            if index > len(number_list) -1:
                start += 1      # increment start and
                preamble += 1   # preamble to get next values for number_list after x+y == self[index] is returned true
                for x in number_list:       # Loop through each value in number_list and compare it to itself
                    for y in number_list:   # Both comparisons have to be different.
                        if x + y == self[index]: 
                            solution_bool = True 
                            break # break out of for y loop
                        else:
                            solution_bool = False
                    if solution_bool: 
                        break # break out of for x loop
                if solution_bool == False: # if solution_bool == False, than no value of x and y returned True for == equaling the value after the preamble.
                    return self[index] # return the value that cannot be solved for. 
            index += 1 # increments index to get preamble and loop through xmas_encryption list.
  
    def find_solution_pt2(self, start, index, preamble, invalid_number):
        ''' 
            TO be updated
        '''
        
        return self

                
with open('inputs/day_09-input.txt', 'r') as input:
    xmas_encryption = [int(input) for input in input.read().splitlines()]
    solution1 = Solution.find_solution_pt1(xmas_encryption, 0, 25, 25)
    solution2 = Solution.find_solution_pt2(xmas_encryption, 0, 1, 1, xmas_encryption.index(solution1))
    print("Solution 1: ", solution1)