# Advent of Code 2020 Day 8 - Handheld Halting

# imports

import re
from collections import defaultdict

class Dictionary:
    def __init__(self, input):
        self.input = input
    
    def create_dictionary(self):
        dictionary = defaultdict(dict)
        for line in self:
            for key, sign, value in re.findall(r'(\w+) ([+-])(\d+)', line):
                dictionary[key] = sign, int(value)
        return dictionary


with open('inputs/day_08-input.txt', 'r') as input:
    code = input.read().splitlines()
    dictionary = Dictionary.create_dictionary(code)