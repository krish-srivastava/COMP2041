#!/usr/bin/env python3

import sys

filename = sys.argv[3]
with open(filename, "w") as file:
    for number in range(int(sys.argv[1]), int(sys.argv[2])+1):
        file.write(str(number) + "\n")
