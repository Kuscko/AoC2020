# Advent of Code 2020 Day 11 - Seating System

class Solutions:
    def __init__(self, data):
        self.data = data

    def find_solution(self, part1=False):
        table = [row.copy() for row in self]
        while True:
            previous_table = [row.copy() for row in table]
            for row in range(len(previous_table)):
                for column in range(len(previous_table[row])):
                    if previous_table[row][column] != '.':
                        adjacent_seats = Calculate.get_adjacent_seats(self, row, column, previous_table, part1)

class Calculate:
    def __init__(self, data):
        self.data = data
    
    def get_adjacent_seats(self, row, column, previous_table, part1):
        seats = 0
        for radj, cadj in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0, -1)]:
            r = row
            c = column
            while True:
                r = r+radj
                c = c+cadj
                if(r < 0 or r >= len(previous_table)) and  

with open('inputs/day_11-input.txt', 'r') as input:
    grid_data = [list(data) for data in input.read().splitlines()]
    print("solution1", Solutions.find_solution(grid_data, part1=True))