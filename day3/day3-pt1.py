import os

def create_list(file_name):
    with(open(file_name) as f):
        return f.read().splitlines()

# fetch file path & create list
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
input_data = create_list(file_path)

# declare constants
line_len = len(input_data[0])
slope = (3, 1)

# declare variables for counter
x_cordinate = 0
tree_count = 0

# loop through each line and if x cordinate in line is "#", increment tree counter
# each value 
for line in input_data:
    if line[x_cordinate] == "#":
        tree_count += 1
    x_cordinate = (x_cordinate + slope[0]) % line_len

print(tree_count)
