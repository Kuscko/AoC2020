# Advent of Code 2020 Day 8 - Handheld Halting

# imports

import re
import numpy as np

class Solutions:
    def __init__(self, input):
        self.input = input

    # def find_solution_pt1(self):
    #     def find_solution(index):
    #         global accumulator
    #         if index not in used:
    #             used.append(index)
    #             row = self[index]
    #             key, sign, value = (row[0], row[1], row[2])
    #             if key == 'acc':
    #                 if sign == '+': 
    #                     accumulator += value 
    #                     return find_solution(index+1)
    #                 else: 
    #                     accumulator -= value
    #                     return find_solution(index+1)
    #             elif key == 'jmp':
    #                 if sign == '+': return find_solution(index+value)

    #                 else: return find_solution(index-value)
    #             else: return find_solution(index+1)
    #         else: 
    #             return accumulator
    #     return find_solution(0)

    def find_solution_pt1(self):
        index_list = set()
        accumulator = 0
        index = 0
        while True:
            row = self[index]
            key, args = (row[0], row[1])
            if index in index_list:
                return accumulator
            index_list.add(index)
            if key == 'acc':
                accumulator += args
                index += 1 
            elif key == 'jmp':
                index += args
            else: 
                index += 1
            

class Arrays:
    def __init__(self, input):
        self.input = input
    
    def create_3d_array(self):
        array = []
        for line in self:
            col = []
            # for key, sign, value in re.findall(r'(\w+) ([+-])(\d+)', line):
            for key, value in re.findall(r'(\w+) ([+-]\d+)', line):
                col += [key, int(value)]
            array.append(col)
        return array


with open('inputs/day_08-input.txt', 'r') as input:
    code = input.read().splitlines()
    dictionary = Arrays.create_3d_array(code)
    solution_1 = Solutions.find_solution_pt1(dictionary)
    accumulator = 0

    print(solution_1)
    accumulator = 0
    print()