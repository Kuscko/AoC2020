# Advent of Code 2020 Day 8 - Handheld Halting

# imports
import re

class Solutions:
    def __init__(self, input):
        self.input = input

    def find_solution_pt1(self, index, bool_value=False):
        '''
            Loop through the given set of boot code instructions and return with the accumulator value for solution 1 & 2.

            Args:
                self -> Bootcode instructions list.
                index -> Index value to loop through insturctions list.
                bool_value -> True if finding the solution for part_one, else False for part_two.
        '''
        index_list = set()
        accumulator = 0
        while True:
            # solution 2 condition:
            # 
            # reach the end of the list by looping through each row.
            # if the end of the list is reached, than the broken instruction in the boot code
            # is fixed and we return the resulting accumulator value.
            if index >= len(self):
                return accumulator
            # Solution 1 condition:
            # 
            # if the index is inside the index_list-set() then return the accumulator value.
            # only return if the bool_value = True, else False.
            # this is to prevent the accumulator value being returned while part2 of the solutions is running
            # to continue looing in find_solution_pt2.
            if index in index_list:
                return accumulator if bool_value else False
            index_list.add(index) # add index value to the index_list set()
            row = self[index] # assign row values based on index and assign values in row.
            key, args = (row[0], row[1]) # ^ as above, so is below.
            # validation for each instruction and changing the index to iterate through the list.
            if key == 'acc':
                accumulator += args
                index += 1 
            elif key == 'jmp':
                index += args
            else: 
                index += 1
            
    def find_solution_pt2(self):
        '''
            Code to switch one jmp or nop argument in self, bootcode instructions through enumeration.

            Args:
                Self -> Bootcode instructions list.
        '''
        for index, args in enumerate(self): # enumerate through bootcode instructions, assign index and args
            if args[0] == 'jmp' or args[0] == 'nop': # check if args[0] = 'nop' or 'jmp'
                previous = args[0] 
                # switch 'nop' to 'jmp' or vice versa.
                if args[0] == 'jmp': self[index][0] = 'nop' 
                elif args[0] == 'nop': self[index][0] = 'jmp'
                # if accumulator returns True, then return accumulator value.
                if accumulator:= Solutions.find_solution_pt1(self, 0):
                    return accumulator
                self[index][0] = previous # if return is not done, undo the previous changes to the args in enumaration.
                

class Arrays:
    def __init__(self, input):
        self.input = input
    
    def create_3d_array(self):
        '''
            Create a 3d array made up of each row in the input.txt file for the bootcode instructions.

            Args:
                self -> raw_data for input.txt
        '''
        array = []
        for line in self: # get the raw_input data of the input.txt file
            col = []
            # for key, value in re.findall(r'(\w+) ([+-]\d+)', line):
            # example: "acc +123" = "(acc) ([+]123)" based on regex above.
            for key, value in re.findall(r'(\w+) ([+-]\d+)', line): 
                col += [key, int(value)] # assign each key, and value to col to create individual lists.
            array.append(col) # append all of col to array.
        return array


with open('inputs/day_08-input.txt', 'r') as input:
    code = input.read().splitlines() # split each line in input.txt
    dictionary = Arrays.create_3d_array(code) # assign array of lists to dictionary
    solution_1 = Solutions.find_solution_pt1(dictionary, 0, True) # assign accumulator value for solution_1
    solution_2 = Solutions.find_solution_pt2(dictionary) # assign accumulator value for solution_2

    print("Solution 1:", solution_1)
    print("Solution 2:", solution_2)