# Advent of Code 2020 Day 7 - Handy Haversacks

'''
    Back burner Part 2.
'''

from collections import defaultdict
import re

class Solution:
    def __init__(self, rules):
        self.rules = rules

    def get_solution_pt1(self, goal):
        '''
            Go through each bag dictionary item and determine which dictionary item has shiny gold bags.
            Then add them to the counter and get the legnth.
            Counter Set is left out side of the definition, although recursion could be used by creating
            a function() inside the method.

            Args:
                Self -> Dictionary{} rules
                goal -> "Shiny Gold" or goal of part 1.
        '''
        for bags in self:
            if goal in self[bags]:
                count.add(bags)
                Solution.get_solution_pt1(self, bags)
        return 

# Dictionary class
class Dictionary:
    def __init__(self, input):
        self.input = input
    
    def create_dictionary(self):
        '''
            Function that creates a dictionary from the passport list under the item arguement
        '''
        dictionary = defaultdict(dict)
        for line in self:
            top_bag = re.match(r'(.*) bags contain', line).group(1)
            for value, key in re.findall(r'(\d+) (\w+ \w+) bag', line):
                dictionary[top_bag][key] = int(value)
        return dictionary

# Create data set of "bag_list"
with open('inputs/day_07-input.txt', 'r' ) as input: 
    bag_rules = input.read().splitlines() # divide each line into a list
    bag_list = Dictionary.create_dictionary(bag_rules) # create the dictionary

    # initialize set() to use as a filter to remove repeatable bag types
    count = set()
    Solution.get_solution_pt1(bag_list, "shiny gold")
    print(len(count))
    

