#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

replacements = {}

for i, line in enumerate(lines):
    if "#" in line:
        target_line = line.strip()[1:]
        if target_line.isdigit():
            replacements[i] = int(target_line)
    else:
        replacements[i] = line.strip()

for key in replacements:
    value = replacements[key]
    if isinstance(value, int):
        replacements[key] = replacements[value - 1]

for key in replacements:
    value = replacements[key]
    print(value)
