# Advent of Code 2020 Day 9 - Encoding Error

import numpy as np

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
  
    def find_solution_pt2(self, invalid_number):
        ''' 
            Loop through each value in xmax_encrytion list and append them to a numpy array using i as the beginning index and j as the ending index. 
            Then we test the sum of the numpy array using .sum() method and check if it equals the invalid number returned from Solution1.

            Args:
                self -> xmas_encryption list of integers.
                invalid_number -> invalid_number found in solution1.
        '''
        for i in range(0, len(self)-1): # range through list, starting at index 0
            for j in range(1, len(self) - 1): # range through list, starting at index 1
                coniguous_array = np.array(self[i:j]) # create numpy array using xmas_encryption list[i:to:j]
                if np.sum(coniguous_array) == invalid_number: # check if sum of np.array = invalid number from solution 1
                    return coniguous_array.min()+coniguous_array.max() # return sum of min/max values in coniguous_array.

                
with open('inputs/day_09-input.txt', 'r') as input:
    xmas_encryption = [int(input) for input in input.read().splitlines()]
    solution1 = Solution.find_solution_pt1(xmas_encryption, 0, 25, 25)
    solution2 = Solution.find_solution_pt2(xmas_encryption, solution1)
    print("Solution 1: ", solution1)
    print("Solution 2: ", solution2)