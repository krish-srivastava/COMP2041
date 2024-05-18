#!/usr/bin/env python3

import sys
import re

string = []

for lines in sys.stdin:
    string.append(lines)

for lines in string:
    pattern = r'[-+]*([0-9]+[\.]?[0-9]*)'
    find = re.findall(pattern, lines)
    if find:
        for nums in find:
            value = round(float(nums))
            lines = re.sub(nums, str(value), lines)
        print(lines, end="")
    else:
        print(lines, end="")