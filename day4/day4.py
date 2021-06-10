# Advent of Code 2020 Day 4

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
    def __init__(self, passport):
        self.passport = passport

    def field_in_passport(self):
        return len(self.passport) == 8 or len(self.passport) == 7 and 'cid' not in self.passport

    def is_valid_year(self, key, min, max):
        return len(self.passport[key]) == 4 and int(self.passport[key]) >= min and int(self.passport[key]) <= max

    def is_valid_byr(self):
        return self.is_valid_year('byr', 1920, 2002)

    def is_valid_iyr(self):
        return self.is_valid_year('iyr', 2010, 2020)
    
    def is_valid_eyr(self):
        return self.is_valid_year('eyr', 2020, 2030)

    def is_valid_hgt(self):
        if self.passport['hgt'][-2:] == "cm":
            return 150 <= int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == "in":
            return 59 <= int(self.passport['hgt'][:-2]) <= 76

    def is_valid_hcl(self):
        return re.compile("^#[0-9a-f]{6}$").search(self.passport['hcl'])

    def is_valid_ecl(self):
        return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_valid_pid(self):
        return len(self.passport['pid']) == 9

    def is_valid_passport(self):
        return (self.is_valid_byr() and self.is_valid_iyr() and self.is_valid_eyr() and self.is_valid_hgt()
        and self.is_valid_hcl() and self.is_valid_ecl() and self.is_valid_pid())

# Dictionary class
class Dictionary:
    def __init__(self, input):
        self.input = input
    
    def create_dictionary(self):
        dictionary = {}
        for line in self:
            key, value = line.split(":")
            dictionary[key] = value
        return dictionary

# main code block
with open('inputs/day_04-input.txt', 'r') as file:
    raw_input1 = file.read().split("\n\n")
    raw_input2 = [raw_input2.replace("\n", " ") for raw_input2 in raw_input1]
    raw_input3 = [raw_input3.split() for raw_input3 in raw_input2]

file.close()

passports = [Dictionary.create_dictionary(line) for line in raw_input3]
valid_passports = [Validation(passport) for passport in passports]
for valid_passport in valid_passports:
    if valid_passport.field_in_passport():
        part1_count += 1
        if valid_passport.is_valid_passport():
            part2_count += 1

print(part1_count)
print(part2_count)