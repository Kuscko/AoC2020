# Advent of Code 2020 Day 6 - Custom Customs


class Unique:
    '''
        Validation for questionair.
    '''

    def __init__(self, input):
        self.lines = input

    def unique_charaters(self):
        '''
            Checks for unique_charaters in each questionair 
        '''
        characters = []
        for char in self:
            if char not in characters:
                characters.append(char)
        return len(characters)

    def get_unique_characters(self):
        '''

        '''
        characters = []
        for char in self[0]:
            NotInLines = True 
            for line in self:
                if char not in line:
                    NotInLines = False
            if NotInLines and char not in characters:
                characters.append(char)
        return len(characters)


# Format lists for the input data
with open('inputs/day_06-input.txt', 'r') as input:
    raw_input1 = input.read().split('\n\n')
    raw_input2 = [raw_input2.split("\n") for raw_input2 in raw_input1]

sum1 = 0
sum2 = 0
string = ""
string2 = []
# loops through each 
for input in raw_input2: 
    for line in input: 
        string += line
        string2.append(line)
    else:
        sum1 += Unique.unique_charaters(string)
        sum2 += Unique.get_unique_characters(input)
        string = ""
        string2 = []


print("Solution 1: ", sum1)
print("Solution 2: ", sum2)