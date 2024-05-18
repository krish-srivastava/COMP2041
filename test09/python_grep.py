#!/usr/bin/env python3

import sys
import re

filename = sys.argv[2]
regex = sys.argv[1]

with open(filename, "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        if re.search(regex, line):
            print(line)    