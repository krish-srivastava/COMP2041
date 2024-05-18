#! /usr/bin/env python3

import sys

number = int(sys.argv[1])

listed_args = {}
count = 0
for arg in sys.stdin:
    listed_args[arg] = listed_args.get(arg, 0) + 1

    if listed_args[arg] == number:
        print("Snap: "+arg, end='')
        break