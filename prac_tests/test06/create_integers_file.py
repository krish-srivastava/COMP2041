#!/usr/bin/env python3

import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
filename = sys.argv[3]

with open(filename, 'w') as file:
    for i in range(start, end):    
        file.write(str(i) + '\n')
    