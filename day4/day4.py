# Advent of Code 2020 Day 4 - Passport Processing

# !MISSING : cid is okay

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def create_dictionary(passports):
    '''
        Convert each passport item into a dictionary item

        Args:
            passports: individual passport stored in the raw_input3 list
        
        return:
            Returns the dictionary object with each passport line added as a key:value
    '''
    dictionary = {}
    for passport in passports:
        key, value = passport.split(':')
        dictionary[key] = value
    return dictionary

def validate_passport(passport) -> bool:
    is_valid_birth_year = "byr" in passport
    is_valid_issue_year = "iyr" in passport
    is_valid_experation_year = "eyr" in passport
    is_valid_height = "hgt" in passport
    is_valid_hair_color = "hcl" in passport
    is_valid_eye_color = "ecl" in passport
    is_valid_passport_id = "pid" in passport
    # is_valid_country_id = "cid" in passport

    return (
        is_valid_birth_year and
        is_valid_issue_year and 
        is_valid_experation_year and 
        is_valid_height and
        is_valid_hair_color and
        is_valid_eye_color and
        is_valid_passport_id 
    )


with open('inputs/day_04-input.txt', 'r') as file:
    raw_input1 = file.read().split('\n\n') # break down each passport into their own list object
    raw_input2 = [raw_input2.replace('\n', ' ') for raw_input2 in raw_input1] # remove newlines within individual passports, replace with spaces
    raw_input3 = [raw_input3.split() for raw_input3 in raw_input2] # split up each seperate value in each passport into their own list 

passports = [create_dictionary(line) for line in raw_input3]
valid_passports = [passport for passport in passports if validate_passport(passport)]

print(
