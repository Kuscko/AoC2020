# Advent of Code 2020 Day 7 - Handy Haversacks

'''
    6/13/2021
    Updates required to comments, due tomorrow morning around 11am.
'''

import re

class Solution:
    def __init__(self, rules):
        self.rules = rules

    def find_goal(self, goal):
        for bag in bag_rules:
            bags = bag_rules[bag]
            if goal in bags:
                Solution.find_goal(self, bag)
                bag_list_count.add(bag)
        return

# Dictionary class
class Dictionary:
    def __init__(self, input):
        self.input = input
    
    def create_dictionary(self):
        '''
            Function that creates a dictionary from the passport list under the item arguement
        '''
        dictionary = {}
        for line in self:
            bags = re.match("(.*) bag contains", line).group()[0]
            for bag in bags:
        return dictionary

# Create data set of "bag_rules"
with open('inputs/day_07-input.txt', 'r' ) as input: 
    raw_input1 = input.read().splitlines() # divide each line into a list
    raw_input2 = [raw_input2.replace(' bags', '').replace('bags,', '').replace('bag,', '').replace('.', '') for raw_input2 in raw_input1] # remove uneccessary information from input strings
    bag_rules = Dictionary.create_dictionary(raw_input2) # create the dictionary
    input.close() # close the input file.
    
    # initialize set() to use as a filter to remove repeatable bag types
    bag_list_count = set()
    Solution.find_goal(bag_rules, "shiny gold")
    print("Solution 1: ", len(bag_list_count))


