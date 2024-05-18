#!/usr/bin/env python3

import sys
import linecache

filename = sys.argv[2]
line_number = int(sys.argv[1])

line = linecache.getline(filename, line_number)

print(line, end='')