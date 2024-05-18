#!/usr/bin/env python3

import sys

read_file = sys.argv[1]

total_lines = 0

with open(read_file, "r") as file1:
    # Count the total amount of lines
    for line in file1:
        total_lines += 1
    
    # Reset the pointer in the file to the start of the file
    file1.seek(0)
    
    # If there's an even count of lines
    if total_lines % 2 == 0:
        print_index_1 = total_lines // 2
        print_index_2 = print_index_1 - 1
        for i, line in enumerate(file1):
            if i == print_index_1:
                print(line.strip())
            if i == print_index_2:
                print(line.strip())

    # If there's an odd count of lines
    if total_lines % 2 == 1:
        print_index = total_lines // 2
        for i, line in enumerate(file1):
            if i == print_index:
                print(line.strip())
        