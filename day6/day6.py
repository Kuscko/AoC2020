# Advent of Code 2020 Day 6 - Custom Customs


class Unique:
    '''
        Validation for questionair.
    '''

    def __init__(self, input):
        self.answerss = input

    def unique_charaters(self):
        '''
            Checks for unique_charaters, or unique yes answers for each questionair.
        '''
        characters = []
        for char in self: # For each character(a-z) in self.input,
            if char not in characters: # if the character isn't in the characters[] list
                characters.append(char) # append the new character to the characters[] list.
        return len(characters) # Return the length(sum total) of that characters[] list.

    def unique_yes_answers(self):
        '''
            Checks for each unique yes answers that match for each answers.
        '''
        characters = []
        for char in self[0]: # For each character(a-z) in self.input[0](first string of list)
            NotInanswerss = True 
            for answers in self: # for each answers STRING in self.input[] list:
                if char not in answers: # if the character(a-z) is not in the STRING answersS (besides the FIRST STRING of the LIST[])
                    NotInanswerss = False # set to false, if not lin answers then the character does not match across each questionaire.
            if NotInanswerss and char not in characters: # If the character(a-z) is unique to each STRING answers in self.input[] list, AND character is not in characters[] list
                characters.append(char) # append the character(a-z) to the character[] list
        return len(characters) # return the length(sum total) of that characters[] list


# Declare variables
part1_sum = 0
part2_sum = 0
questionare_string = ""

# Format lists for the input data
with open('inputs/day_06-input.txt', 'r') as input:
    raw_input1 = input.read().split('\n\n')
    questionairs = [questionairs.split("\n") for questionairs in raw_input1]


# loops through each questionaire in questionairs[] list
for questionaire in questionairs: 
    for answers in questionaire: # appends each of the answers in the individual questionaire(s) to a string
        questionare_string += answers 
    else:
        part1_sum += Unique.unique_charaters(questionare_string) # sum total of each length of the questionare string, with no repeat answers.
        part2_sum += Unique.unique_yes_answers(questionaire) # sum total of each yes answers of the same character(a-z)
        # clears the string and list
        questionare_string = ""
        part2_string = []


print("Solution 1: ", part1_sum)
print("Solution 2: ", part2_sum)