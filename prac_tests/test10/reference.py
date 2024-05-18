#! /usr/bin/env python3

import sys
import re

string = []

for line in sys.stdin:
    string.append(line)

for line in string:
    pattern = r'#([0-9])+'
    matches = re.search(pattern, line)
    if matches:
        index = int(matches.group(1)) - 1
        print(string[index], end="")
    else:
        print(line, end="")
    