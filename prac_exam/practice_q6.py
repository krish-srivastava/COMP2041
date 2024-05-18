#!/usr/bin/env python3

import sys

filename_1 = sys.argv[1]
filename_2 = sys.argv[2]

if len(sys.argv) < 2:
    print("Please specify two files")
    exit(1)

lines_1 = None
lines_2 = None

with open(filename_1, "r") as file1:
    lines_1 = file1.readlines()

with open(filename_2, "r") as file2:
    lines_2 = file2.readlines()

lines_1_len = len(lines_1)
lines_2_len = len(lines_2)

if (lines_1_len != lines_2_len):
    print(f"Not mirrored: different number of lines: {lines_1_len} versus {lines_2_len}")
    exit(2)

mismatch_line = -1

for i, (line1, line2) in enumerate(zip(lines_1, reversed(lines_2))):
    if (line1.strip() != line2.strip()):
        mismatch_line = i
        break;

if mismatch_line != -1:
    print(f"Not mirrored: line {mismatch_line} different")
    exit(3)

print("Mirrored")