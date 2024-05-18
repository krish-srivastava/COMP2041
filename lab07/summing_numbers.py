#!/usr/bin/env python3
import re
import sys

# Check if a filename argument is provided
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument.")
    sys.exit(1)

filenames = sys.argv[1:]

numbers = []

for filename in filenames:
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            matches = re.findall(r'\d+', line)  # Find all numeric sequences in the line
            numbers.extend(matches)

sum = 0
for number in numbers:
    sum = sum + int(number)

print(sum)