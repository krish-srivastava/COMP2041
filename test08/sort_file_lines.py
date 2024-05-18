#!/usr/bin/env python3
import sys

def sort_by_line_length(filename):
    with open(filename, "r") as file1:
        lines = file1.readlines()

    sorted_lines = sorted(lines, key=lambda line: (len(line), line))

    for line in sorted_lines:
        print(line.strip())

filename = sys.argv[1]

sort_by_line_length(filename)