#!/usr/bin/env python3

import re
import sys

# Check if a filename argument is provided
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument.")
    sys.exit(1)

filenames = sys.argv[1:]

orca_count = 0

for filename in filenames:
    with open(filename, 'r') as file:
        for line in file:
            if re.search(r'Orca', line):
                columns = line.strip().split()
                orca_count = orca_count + int(columns[1])

output = str(orca_count) + " Orcas reported"
print(output)