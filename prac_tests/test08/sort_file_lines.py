#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name, "r") as file:
    lines = file.readlines()
    lines.sort()
    lines.sort(key=len)
    print("".join(lines), end="")    
    