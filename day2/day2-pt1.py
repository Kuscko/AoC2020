# Advent of Code: Day 2 - Part 1
# completed by Patrick Kelly 5/30/2021 | 11:04AM

import os

# get file path of input.txt
file_path = os.path.join(os.path.dirname(__file__),'input.txt')

valid_counter = 0

with open(file_path, 'r') as file:
    input = file.read().splitlines()
    for string in input:
        # splits the string into 3 parts
        # 1: #-# the min/max values for the policy.
        # 2: C: the caracter that the policy requires.
        # 3: ^0-9: The policy password to validate against.
        raw_string = string.split()

        # splits the part(#1) to get the min/max values of the policy.
        policy_string = raw_string[0].split("-")
        # get values
        min = int(policy_string[0])
        max = int(policy_string[1])

        # gets the character that the policy requires (#2).
        character = raw_string[1][0]

        # defines the password and counts the required characters in the password
        password = raw_string[2]
        character_count = password.count(character)

        #checks if the character_count in the password is greater than or equal to the min count
        if character_count >= min:
            # if true: checks if the character count is less then or equal to the max count
            if character_count <= max:
                valid_counter += 1

print("Valid passwords: ", valid_counter)

