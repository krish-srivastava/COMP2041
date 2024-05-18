#!/usr/bin/env python3
import sys
import linecache

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1, "r") as file:
    lines = file.readlines()

lines.reverse()

with open(filename2, "w") as file:
    file.writelines(lines)
