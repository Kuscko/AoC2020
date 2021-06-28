# Advent of Code 2020 Day 4 - Passport Processing

import re

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

cid is not required
'''

# declare iterable variables
part1_count = 0
part2_count = 0


# Validation class
class Validation:
    '''
        Validation for each passport against criteria for each field.    
    '''


    def __init__(self, passport):
        self.passport = passport

    def field_in_passport(self):
        '''
            Checks each passport if it has 8 fields or 7 fields and not country ID(cid)
        '''
        return len(self.passport) == 8 or len(self.passport) == 7 and 'cid' not in self.passport

    def is_valid_year(self, key, min, max):
        '''
            Function that checks the year is correct using the given arguments.

            Args:
                key: key to the passport dictionary being validated.
                min: minimal value checked against.
                max: maximum value checked against.

            If the length of the passport[key] value == 4 and if the passport[key] value is between the min/max values.
        '''
        return len(self.passport[key]) == 4 and max >= int(self.passport[key]) >= min 

    def is_valid_byr(self):
        '''
            Validates birth Year.
        '''

        return self.is_valid_year('byr', 1920, 2002)

    def is_valid_iyr(self):
        '''
            Validates issue Year
        '''
        return self.is_valid_year('iyr', 2010, 2020)
    
    def is_valid_eyr(self):
        '''
            Validates expiration year
        '''
        return self.is_valid_year('eyr', 2020, 2030)

    def is_valid_hgt(self):
        '''
            Validates the passport['hgt'] - height value in the passport.
            if the unit measurement is in 'cm' centimeters then the validation 
            is different compared to 'in' inches. 
        '''
        if self.passport['hgt'][-2:] == "cm":
            return 150 <= int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == "in":
            return 59 <= int(self.passport['hgt'][:-2]) <= 76

    def is_valid_hcl(self):
        '''
            Validates the haircolor (hcl) hexidecimals using a regex that checks 
            if the first character is a "#" pound sign, then if the next 
            characters are numerical and have letters a-f. 
            It also determines if it is exactly 6 characters long.
        '''
        return re.compile("^#[0-9a-f]{6}$").search(self.passport['hcl'])

    def is_valid_ecl(self):
        '''
            Validates the eye color (ecl) if it has a value in one of the colors in the list
        '''
        return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_valid_pid(self):
        '''
            determines if the passport['pid'] passport ID is only 9 characters in length
        '''
        return len(self.passport['pid']) == 9

    def is_valid_passport(self):
        '''
            Calls for the validation functions for each passport and returns a bool
        '''
        return (self.is_valid_byr() and self.is_valid_iyr() and self.is_valid_eyr() and self.is_valid_hgt()
        and self.is_valid_hcl() and self.is_valid_ecl() and self.is_valid_pid())

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
            key, value = line.split(":")
            dictionary[key] = value
        return dictionary

# main code block
with open('inputs/day_04-input.txt', 'r') as file:
    raw_input1 = file.read().split("\n\n") # splits up each passport at the double \n new lines.
    raw_input2 = [raw_input2.replace("\n", " ") for raw_input2 in raw_input1] # replaces other \n newlines within each passport with a space.
    raw_input3 = [raw_input3.split() for raw_input3 in raw_input2] # splits each passport up into their indiviudal components.

file.close() # closses file day_04-input.txt

passports = [Dictionary.create_dictionary(line) for line in raw_input3] # creates a dictionary using the create_dictionary method using each line in raw_input3
valid_passports = [Validation(passport) for passport in passports] # initializes individual Validation objects by each pasport.
for valid_passport in valid_passports:
    # validates each passport based on part 1 and part 2 of the day 4 requirements. 
    if valid_passport.field_in_passport():
        part1_count += 1
        # nested if statement to prevent KeyErrors during validation
        if valid_passport.is_valid_passport():
            part2_count += 1

print(part1_count)
print(part2_count)