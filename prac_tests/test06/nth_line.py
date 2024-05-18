#!/usr/bin/env python3

import sys

number_line = int(sys.argv[1])
filename = sys.argv[2]

with open(filename, "r") as file:
    lines = file.readlines()
    
    for i, line in enumerate(lines):
        if ((i + 1) == number_line):
            print(line.strip())